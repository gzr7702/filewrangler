from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Phil has heard about a managed file transfer website
        # He goes to the homepage:
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention filewrangerl
        self.assertIn('File Wrangler', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('File Wrangler', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_file')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a file name'
        )

#===========================================================================================
        #She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taken to a new URL,
        #and now the paget lists "1: Buy peacock feathers" as an item on a 
        #to-do list table
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/list/.+')

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her ot add another item. She
        # enters "Use peacock feathers to make a fly" (Edisth is very methodical)
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn(
            "2: Use peacock feathers to make a fly", 
            [row.text for row in rows]
        )

        #Now a new user, Francis, comes along to the site.
        self.browser.quit()
        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies, etc.
        self.browser = webdriver.Firefox()

        #Francis visits the home page, there is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #Francis starts a new list by entering a new item. He is
        #less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Francis gets his own unique url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again, there is no trace of Edith's list
        page_text = self.browser.fine_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock featehrs', page_text)
        self.assertIn('Buy mil', page_text)

        # Satisfied, she goes back to sleep


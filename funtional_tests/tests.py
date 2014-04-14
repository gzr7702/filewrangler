from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_a_new_scheduled_transfer(self):
        # Phil has heard about a managed file transfer website
        # He goes to the homepage:
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention filewrangerl
        self.assertIn('File Wrangler', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('File Wrangler', header_text)

        # He is invited to enter a new file object 
        # First, he enters the src of the transfer:
        #inputbox = self.browser.find_element_by_id('id_new_file')
        #self.assertEqual(
        #    inputbox.get_attribute('placeholder'),
        #    'Enter a file name'
        #)

        # Next, he enters the destination of the transfer:

        # Then, he chooses if he wants to compress or uncompress the file

        #Next, he enters a scheduled time for the transfer

        # Finally, he adds an email address to receive an alert about the transfer.

        # He clicks 'save', and he is redirected to the display page of all transfers.


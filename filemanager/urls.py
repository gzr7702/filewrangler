from django.conf.urls import patterns, include, url

from filemanager import views

urlpatterns = patterns('',
    url(r'^$', 'views.home_page', name='home'),
    )


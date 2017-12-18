#!/usr/bin/venv python

from selenium import webdriver

from django.test import TestCase, LiveServerTestCase

class ApiTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.get(self.live_server_url)
    pass
  def tearDown(self):
    self.browser.quit()

  def test_can_open_home_page(self):
    self.assertEqual('1', '1')

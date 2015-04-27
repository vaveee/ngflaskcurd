# -*- coding:utf-8 -*-
import random
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re


class BaseSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
    def login(self, login_username, password):
        self.driver.get(self.base_url + "/accounts/login")
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys(login_username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def logout(self):
        self.driver.find_element_by_link_text(u"注销").click()
        
    def sleep(self, sec = 1):
        time.sleep(sec)

    def random(self, length = 5):
        _ = str(random.randint(10 ** length, 10 ** (length + 1)))
        return _[0:length]

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
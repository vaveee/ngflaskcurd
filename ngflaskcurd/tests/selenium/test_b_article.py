# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from base import BaseSelenium

class SeleniumTest(BaseSelenium):
    
    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "/bg")
        self.login('admin', '123456')

        driver.get(self.base_url + "bg/notice/article_list")

        #增加
        for i in range(20):
            driver.get(self.base_url + "bg/notice/article_add")
            driver.find_element_by_id("title").clear()
            driver.find_element_by_id("title").send_keys(u"文章")
            driver.find_element_by_id("title").send_keys(i)
            driver.find_element_by_xpath("//button[@type='submit']").click()
#            
#        #翻页
#        driver.get(self.base_url + "train_list")
#        #time.sleep(2)
#        driver.find_element_by_css_selector("div.panel-body > a").click()
#        #time.sleep(2)
#        driver.find_element_by_link_text(u"下一页 >>").click()
#        #time.sleep(2)
#        driver.find_element_by_link_text(u"<< 上一页").click()
        

if __name__ == "__main__":
    unittest.main()

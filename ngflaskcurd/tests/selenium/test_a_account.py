# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from base import BaseSelenium

class Employee(BaseSelenium):
    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "accounts/register")
        
        
        #注册
#        for i in range(20):
#            driver.get(self.base_url + "employee/employee_add")
#            driver.find_element_by_id("name").clear()
#            driver.find_element_by_id("name").send_keys(u"张老")
#            driver.find_element_by_id("name").send_keys(i)
#            
#            driver.find_element_by_id("phone").clear()
#            driver.find_element_by_id("phone").send_keys(u"1333333333")
#            driver.find_element_by_id("phone").send_keys(i)
#            
#            driver.find_element_by_id("doc").clear()
#            driver.find_element_by_id("doc").send_keys(u"3")
#            driver.find_element_by_id("doc").send_keys(i)
#            
#            driver.find_element_by_id("con_code").clear()
#            driver.find_element_by_id("con_code").send_keys(u"3")
#            driver.find_element_by_id("con_code").send_keys(i)
#            
#            driver.find_element_by_id("entry_date").clear()
#            driver.find_element_by_id("entry_date").send_keys(u"2014-06-16")
#            
#            driver.find_element_by_id("positive_date").clear()
#            driver.find_element_by_id("positive_date").send_keys(u"2014-07-16")
#            
#            driver.find_element_by_id("end_date").clear()
#            driver.find_element_by_id("end_date").send_keys(u"2015-06-16")
#            
#            
#            #time.sleep(2)
#            driver.find_element_by_id("name").send_keys(Keys.RETURN)
#            
#        #翻页
#        driver.get(self.base_url + "employee/employee_list")
#        #time.sleep(2)
#        driver.find_element_by_link_text(u"下一页 >>").click()
#        #time.sleep(2)
#        driver.find_element_by_link_text(u"<< 上一页").click()

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select 
import time
import pdb

class Controller(object):
   def __init__(self, browser="firefox",username = "" ,password = ""):
       if browser == "firefox":
          self.driver = webdriver.Firefox()
       else:
          self.driver = webdriver.Chrome()

       self.driver.get("http://61.16.140.205:2814/")
       print(self.driver.title)
       assert "Cisco" in self.driver.title
       self.driver.find_element_by_name("bSubmit ").click()
       time.sleep(1)
       self.driver.switch_to.alert.send_keys(username + Keys.TAB + password)
       time.sleep(1)
       self.driver.switch_to.alert.accept()
       self.driver.implicitly_wait(10)
       self.driver.find_element_by_link_text("Advanced").click()
       self.driver.implicitly_wait(10)

   def delete_wlan(self):


       self.driver.get("http://61.16.140.205:2814/screens/frameWlan.html")
       print(self.driver.title)
       assert "Wlan" in self.driver.title

       frame = self.driver.find_element_by_xpath('//frame[@name="content"]')
       self.driver.switch_to.frame(frame)
       self.driver.implicitly_wait(2)
       time.sleep(5)

       self.wlan_id = 10
       no_of_wlans = len(self.driver.find_elements_by_xpath("//table[@cellspacing='1']/tbody/tr")) - 1
       print('wlans = {}'.format(no_of_wlans))

       for i in range(1, no_of_wlans):
          if (self.wlan_id == int(self.driver.find_elements_by_xpath("//table[@cellspacing='1']/tbody/tr")[i].find_element_by_xpath(".//input[@class='statictextboxlink']").get_attribute('value'))):

             popupid = 'popupId' + str(i - 1)
             print(popupid)
             elem = self.driver.find_element_by_id(popupid)
             ActionChains(self.driver).move_to_element(elem).perform()
             time.sleep(5)
             self.driver.find_elements_by_link_text("Remove")[i - 1].click()
             time.sleep(2)
             self.driver.switch_to.alert.accept()
             break;

   def create_open_wlan(self):

       self.driver.get("http://61.16.140.205:2814/screens/frameWlan.html")
       print(self.driver.title)
       assert "Wlan" in self.driver.title

       frame = self.driver.find_element_by_xpath('//frame[@name="content"]')
       self.driver.switch_to.frame(frame)
       self.driver.implicitly_wait(2)
       time.sleep(5)


       self.driver.find_element_by_xpath("//select[@name='wlanaction']/option[text()='Create New']").click()
       self.driver.find_element_by_css_selector('.buttonstretch').click()
       self.driver.implicitly_wait(5)

       self.driver.find_element_by_name("vap_profileName").send_keys('script')
       self.driver.find_element_by_name("vap_ssid").send_keys('script')
       self.driver.find_element_by_xpath("//select[@name='selwlanid']/option[text()='%s']" % self.wlan_id).click()
       self.driver.find_element_by_xpath("//input[@name='apply']").click()
       self.driver.implicitly_wait(3)

       self.driver.find_element_by_xpath("//input[@name='vap_admin_status']").click()

       self.driver.find_element_by_xpath("//span[text()='Security']").click()
       self.driver.find_element_by_xpath("//select[@name='sWep']/option[text()='None']").click()
       self.driver.find_element_by_xpath("//input[@name='apply']").click()
       self.driver.implicitly_wait(5)

       self.driver.find_element_by_xpath("//input[@name='back']").click()


   def disconnect(self):
       self.driver.implicitly_wait(10)
       print('successfully completed')
       self.driver.close()

if __name__ == '__main__':
   my_object = Controller(browser="firefox",username = "admin" ,password = "Admin123")
   my_object.delete_wlan()
   my_object.create_open_wlan()
   my_object.delete_wlan()
   my_object.disconnect()

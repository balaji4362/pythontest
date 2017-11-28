import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select 
import time
import pdb

driver = webdriver.Firefox()
driver.get("http://61.16.140.205:2814/")
print(driver.title)
assert "Cisco" in driver.title
driver.find_element_by_name("bSubmit ").click()
time.sleep(3)
driver.switch_to.alert.send_keys('admin' + Keys.TAB + 'Admin123')
time.sleep(3)
driver.switch_to.alert.accept()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Advanced").click()
driver.implicitly_wait(10)
#driver.find_element_by_link_text('<u>W</u>LANs').click()
#driver.find_element_by_css_selector("//*[href='frameWlan.html']").click()
#driver.find_element_by_xpath("//*[@accesskey='W']").click()
#Actions keyAction = new Actions(driver)     
#keyAction.keyDown(Keys.ALT).keyDown(Keys.SHIFT).sendKeys("w").keyUp(Keys.ALT).keyUp(Keys.SHIFT).perform()
#ActionChains(driver).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys('w').key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//select[@name='wlanaction']/option[text()='Create New']").click()

frame = driver.find_element_by_xpath('//frame[@name="banner"]')
driver.switch_to.frame(frame)
driver.find_element_by_id("cWlans").click()
driver.implicitly_wait(3)
driver.switch_to_default_content()


frame = driver.find_element_by_xpath('//frame[@name="mainFrame"]')
driver.switch_to.frame(frame)
frame = driver.find_element_by_xpath('//frame[@name="content"]')
driver.switch_to.frame(frame)
driver.implicitly_wait(2)
time.sleep(5)

wlan_id = 10
no_of_wlans = len(driver.find_elements_by_xpath("//table[@cellspacing='1']/tbody/tr")) - 1
print('wlans = {}'.format(no_of_wlans))

for i in range(1, no_of_wlans):
   if (wlan_id == int(driver.find_elements_by_xpath("//table[@cellspacing='1']/tbody/tr")[i].find_element_by_xpath(".//input[@class='statictextboxlink']").get_attribute('value'))):

       popupid = 'popupId' + str(i - 1)
       print(popupid)
       elem = driver.find_element_by_id(popupid)
       ActionChains(driver).move_to_element(elem).perform()
       time.sleep(5)
       driver.find_elements_by_link_text("Remove")[i - 1].click()
       time.sleep(2)
       driver.switch_to.alert.accept()
       break;


time.sleep(10)

driver.find_element_by_xpath("//select[@name='wlanaction']/option[text()='Create New']").click()
driver.find_element_by_css_selector('.buttonstretch').click()
driver.implicitly_wait(5)

#driver.find_element_by_xpath("//select[@name='lan_type']/option[text()='WLAN']").click()
driver.find_element_by_name("vap_profileName").send_keys('script')
driver.find_element_by_name("vap_ssid").send_keys('script')
driver.find_element_by_xpath("//select[@name='selwlanid']/option[text()='%s']" % wlan_id).click()
driver.find_element_by_xpath("//input[@name='apply']").click()
driver.implicitly_wait(3)

driver.find_element_by_xpath("//input[@name='vap_admin_status']").click()

driver.find_element_by_xpath("//span[text()='Security']").click()
driver.find_element_by_xpath("//select[@name='sWep']/option[text()='None']").click()
driver.find_element_by_xpath("//input[@name='apply']").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@name='back']").click()

'''
time.sleep(5)
elem = driver.find_element_by_id("popupId0")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(10)
driver.find_element_by_link_text("Remove").click()
time.sleep(2)
driver.switch_to.alert.accept()
'''

no_of_wlans = len(driver.find_elements_by_xpath("//table[@cellspacing='1']/tbody/tr")) - 1
print('wlans = {}'.format(no_of_wlans))

for i in range(1, no_of_wlans):
   if (wlan_id == int(driver.find_elements_by_xpath("//table[@cellspacing='1']/tbody/tr")[i].find_element_by_xpath(".//input[@class='statictextboxlink']").get_attribute('value'))):

       popupid = 'popupId' + str(i - 1)
       print(popupid)
       elem = driver.find_element_by_id(popupid)
       ActionChains(driver).move_to_element(elem).perform()
       time.sleep(5)
       driver.find_elements_by_link_text("Remove")[i - 1].click()
       time.sleep(2)
       driver.switch_to.alert.accept()
       break;

#pdb.set_trace()

driver.implicitly_wait(10)
print('successfully completed')
assert "No results found." not in driver.page_source
driver.close()

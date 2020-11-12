import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://etrak-ne1.com/etrak/cp?org=98&orgin=https://www.ridgefieldparksandrec.org/"

path = r'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)

driver.get(url)

# trigger popup
element = driver.find_element_by_id('siteContainer')
element.click()
element = driver.find_element_by_id('menu')
element = driver.find_element_by_id('signinIcon')
element = driver.switch_to.active_element
element.click()

# close out of popup
element.send_keys(Keys.ESCAPE)

# sign in
element = driver.find_element_by_id('siteContainer')
element.click()
element = driver.find_element_by_id('menu')
element = driver.find_element_by_id('signinIcon')
element.click()

# element = driver.find_element_by_id('signinIcon')
# element = driver.switch_to.active_element
# element.click()

# element = driver.switch_to.active_element
# element = driver.find_element_by_id('')

# element = driver.find_element_by_xpath("//")
# element = driver.find_element_by_xpath(
#     "//div[@class='fancybox-overlay fancybox-overlay-fixed']")
# username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")

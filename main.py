import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

# get login info
with open("client_secret.json", "r") as f:
    login_info = json.load(f)
email = login_info["email"]
password = login_info["pass"]


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
driver.implicitly_wait(10)  # search for popup for 10 seconds
element.send_keys(Keys.ESCAPE)

# start sign in
element = driver.find_element_by_id('siteContainer')
element.click()
element = driver.find_element_by_id('menu')
element = driver.find_element_by_id('signinIcon')
element.click()

# select sign in pop up
element = driver.find_element_by_xpath(
    "/html[@class='sb-init fancybox-lock']/body[@class='primaryBackground']/div[@class='fancybox-overlay fancybox-overlay-fixed']/div[@class='fancybox-wrap fancybox-desktop fancybox-type-iframe fancybox-opened']/div[@class='fancybox-skin']/div[@class='fancybox-outer']/div[@class='fancybox-inner']")

# switch to iframe of sign in
iframe_list = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(1)
element = driver.find_element_by_xpath(
    "//div[@class='form-container']/form[@id='signinForm']/input[@id='username']")

# enter login info
element.send_keys(email)

element = driver.find_element_by_xpath(
    "//div[@class='form-container']/form[@id='signinForm']/input[@id='password']")
element.send_keys(password)

element = driver.find_element_by_xpath(
    "//div[@class='form-container']/form[@id='signinForm']/input[@id='signin']")
# complete sign in
element.click()

# close out of 'success' dialogue box
element = driver.switch_to.parent_frame()
element = driver.find_element_by_xpath(
    "/html[@class='sb-init']/body[@class='primaryBackground stop-scrolling']/div[@class='sweet-alert showSweetAlert visible']/div[@class='sa-button-container']/div[@class='sa-confirm-button-container']/button[@class='confirm']")
element.click()

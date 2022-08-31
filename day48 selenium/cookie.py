from asyncore import loop
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver="/Users/liul85/Downloads/WebDriver/bin/chromedriver"

driver=webdriver.Chrome(chromedriver)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie=driver.find_element_by_id("cookie")

start=time.time()
while time.time() < start+200:
    cookie.click()

#bom update can't find the element,so need to find by element when use it
buyGrandma=driver.find_element_by_id("buyGrandma")
while driver.find_element_by_id("buyGrandma").get_attribute("class")=="":
    driver.find_element_by_id("buyGrandma").click()
    time.sleep(1)

# buyCursor= driver.find_element_by_id("buyCursor")
while driver.find_element_by_id("buyCursor").get_attribute("class")=="":
    driver.find_element_by_id("buyCursor").click()
    time.sleep(1)

cps = driver.find_element_by_id("cps")
print(cps.text)

driver.close()
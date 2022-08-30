from cmath import nan
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
import pandas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

data = pandas.read_csv('check lexile book/booklist.csv')
chrome_driver_path="/Users/liul85/Downloads/WebDriver/bin/chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

url="https://wml.spydus.com/cgi-bin/spydus.exe/MSGTRN/WPAC/HOME"
driver.get(url)

#login to the library
driver.find_element_by_id("navbarLoginMenuLink").click()
driver.find_element_by_id("user_name").send_keys(os.environ.get("WMLID"))
driver.find_element_by_id("user_password").send_keys(os.environ.get("WMLPSW"))
driver.find_element_by_class_name("btn-submit").click()

#find the book and reserver
for i in range(len(data["book"])):
    if data["lexile"][i] > 800:
        search=data["book"][i]+" "+data["author"][i]
        driver.find_element_by_id("header-search-entry").send_keys(search)
        driver.find_element_by_id("header-search-submit").click()
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"),f'Anywhere: {search} (Keywords)'))

        if driver.find_element_by_class_name("highlight").text.lower()==data["book"][i].lower():
            driver.find_element_by_xpath('//*[@id="result-content-list"]/fieldset[1]/div/div[2]/div[2]/div[1]/div[2]/div/a[1]').click()
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "submitButton")))
            driver.find_element_by_id("submitButton").click()
        data["reserved"][i]= "true"

data.to_csv('check lexile book/booklist.csv', index=False)
driver.close()
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pandas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math


data = pandas.read_csv('check lexile book/booklist.csv')
print(data)
chrome_driver_path="/Users/liul85/Downloads/WebDriver/bin/chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

url="https://hub.lexile.com/find-a-book/search"
driver.get(url)


#search and update the lexile
for i in range(len(data["book"])):
    if math.isnan(data["lexile"][i]):
        driver.find_element_by_name("quickSearch").send_keys(Keys.COMMAND,"a")
        driver.find_element_by_name("quickSearch").send_keys(Keys.DELETE)
        driver.find_element_by_name("quickSearch").send_keys(data["book"][i])
        driver.find_element_by_class_name('search').click()
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "search-term"),data["book"][i]))
        if driver.find_element_by_class_name("sc-zjkyB").text.lower() == data["book"][i].lower():
            data["lexile"][i]=driver.find_element_by_class_name("sc-bQFuvY").text
            data["author"][i]=driver.find_element_by_class_name("sc-dXNJws").text[3:]
            print(f'{data["book"][i]} lexile is {driver.find_element_by_class_name("sc-bQFuvY").text}')
        else :
            print(f'the book is {driver.find_element_by_class_name("sc-zjkyB").text}')

driver.close()

data.to_csv('check lexile book/booklist.csv', index=False)

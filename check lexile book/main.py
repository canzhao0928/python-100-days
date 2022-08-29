from cmath import nan
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
import pandas


data = pandas.read_csv('./booklist.csv')

chrome_driver_path="/Users/liul85/Downloads/WebDriver/bin/chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

url="https://hub.lexile.com/find-a-book/search"
driver.get(url)


#search and update the lexile
for i in range(len(data["book"])):
    if data["lexile"][i] == nan:
        driver.find_element_by_name("quickSearch").send_keys(Keys.COMMAND,"a")
        driver.find_element_by_name("quickSearch").send_keys(Keys.DELETE)
        driver.find_element_by_name("quickSearch").send_keys(data["book"][i])
        driver.find_element_by_class_name('search').click()
        # while driver.current_url==url:
        time.sleep(10)
        WebDriverWait(driver,10)
        if driver.find_element_by_class_name("sc-zjkyB").text.lower() == data["book"][i].lower():
            data["lexile"][i]=driver.find_element_by_class_name("sc-bQFuvY").text
            print(f'{data["book"][i]} lexile is {driver.find_element_by_class_name("sc-bQFuvY").text}')
        else :
            print(f'the book is {driver.find_element_by_class_name("sc-zjkyB").text}')

driver.close()

data.to_csv('./booklist.csv', index=False)

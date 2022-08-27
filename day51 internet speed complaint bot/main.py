from unittest import result
from selenium import webdriver
import time

chrome_driver_path="/Users/liul85/Downloads/WebDriver/bin/chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

#do speed test and get the result
url="https://www.speedtest.net/"
driver.get(url)
driver.find_element_by_class_name("start-text").click()
while driver.current_url == url:
    time.sleep(10)
download_speed=driver.find_element_by_class_name("download-speed").text
upload_speed=driver.find_element_by_class_name("upload-speed").text
result_id=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
print(f"resultId is {result_id},download speed is {download_speed}, upload speed is {upload_speed}")
driver.close()

#open twitter and complaint, update later
# url="https://twitter.com/"
# driver.get(url)
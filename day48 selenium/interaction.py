from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver="/Users/liul85/Downloads/WebDriver/bin/chromedriver"

driver=webdriver.Chrome(chromedriver)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fName= driver.find_element_by_name('fName')
fName.send_keys("mark")

lName= driver.find_element_by_name('lName')
lName.send_keys("liu")

email= driver.find_element_by_name('email')
email.send_keys("mark@123.com")

submit=driver.find_element_by_tag_name("button")
submit.send_keys(Keys.ENTER)

# driver.close()
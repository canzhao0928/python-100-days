from tkinter import E
from selenium import webdriver

chrome_driver_path="/Users/liul85/Downloads/WebDriver/bin/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

times =driver.find_elements_by_css_selector(".event-widget time")
events =driver.find_elements_by_css_selector(".event-widget .menu a")
event_upcoming_list={}

for i in range(len(times)):
    event_upcoming_list[i]= {
        "time": times[i].text,
        "name": events[i].text
    }
print(event_upcoming_list)

# close the tab
driver.close()

#quit the browser
# driver.quit()

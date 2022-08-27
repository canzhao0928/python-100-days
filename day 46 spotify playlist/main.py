from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.billboard.com/charts/hot-100/2003-10-04/")

data = response.text

soup= BeautifulSoup(data, "html.parser")
all_title = soup.find_all(name="h3", class_="a-font-primary-bold-s" )
title_list=[]
for title in all_title:
    title_list.append(title.getText().strip())

play_list=title_list[2:]

# only get the songs, doesn't add to spotify

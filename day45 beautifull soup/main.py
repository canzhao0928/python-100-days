from cgi import print_arguments
import requests
from bs4 import BeautifulSoup

# ---------scraping the most popular article--------------
response = requests.get("https://news.ycombinator.com/")
news = response.text

soup= BeautifulSoup(news,"html.parser")
all_articles = soup.find_all(name="a", class_="titlelink")
all_scores = soup.find_all(name="span", class_="score")

title_list =[]
link_list=[]
score_list=[]
for article in all_articles:
    title_list.append(article.getText())
    link_list.append(article.get("href"))
for s in all_scores:
    score= int(s.getText().split()[0])
    score_list.append(score)

print(score_list.index(max(score_list)))

#------scraping top 100 movies-------------
# response=requests.get("https://www.empireonline.com/movies/features/best-movies-2022/")
# data = response.text

# soup= BeautifulSoup(data,"html.parser")
# movies = soup.find_all(name='h3')
# print(movies)
# movie_list=[]
# for movie in movies:
#     movie_list.append(movie.getText())
# print(movie_list)
# class_="jsx-4245974604"

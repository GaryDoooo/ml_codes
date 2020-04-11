from bs4 import BeautifulSoup
import requests
import pickle
import re

url = "http://duonaolive.com/detail?id=51848"
what = Beautiful things.

reading = requests.get(url)

soup = BeautifulSoup(reading.text, "lxml")
#  trlist = soup.table.find_all('tr')
#  trlist = trlist[1:]
#  print([ _.text for _ in soup.find_all('h1')])
#  print([ _.text for _ in soup.find_all('a',href=True)])
season_title = soup.find_all('h1')[0].text

for a in soup.find_all('a', href=True):
    t = a.text.replace('\n', '')
    l = a['href']
    if "../play" in l:
        print(
            l.replace("..", "http://duonaolive.com"),
            (season_title+t).replace(" ", "")
        )

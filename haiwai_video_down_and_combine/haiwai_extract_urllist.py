from bs4 import BeautifulSoup
import requests
#  import pickle
#  import re
url = "https://www.haiwai.tv/index.php/voddetail/31200.html"
reading = requests.get(url)
soup = BeautifulSoup(reading.text, "lxml")
#  trlist = soup.table.find_all('tr')
#  trlist = trlist[1:]
#  print([ _.text for _ in soup.find_all('h1')])
#  print([ _.text for _ in soup.find_all('a',href=True)])
season_title = soup.find_all('h1')[0].text
print(season_title)
playlist1_html = soup.find("div", {"id": "play_down1"})
print(playlist1_html)
#  list1_soup = BeautifulSoup(playlist1_html, "lxml")
for a in playlist1_html.find_all('a', href=True):
    t = a.text.replace('\n', '')
    l = a['href']
    #  if "31200" in l:
    print(
        "https://www.haiwai.tv" + l,
        #  .replace("..", "http://duonaolive.com"),
        (season_title + t).replace(" ", "")
    )
    #  https://www.haiwai.tv/index.php/vodplay/31200-1-1.html

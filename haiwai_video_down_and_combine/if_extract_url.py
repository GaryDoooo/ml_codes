import sys
import re
from playwright.sync_api import sync_playwright
url = sys.argv[1]
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    #  ua = page.query_selector("01")
    atxt = page.eval_on_selector_all(
        "a", "elements => elements.map(element => element.text)")
    aurl = page.eval_on_selector_all(
        "a", "elements => elements.map(element => element.href)")
    links = set()
    for i in range(len(atxt)):
        if "?id=" not in aurl[i]:
            continue
        try:
            e = int(atxt[i].replace(' ', ''))
            #  print(e, aurl[i])
            links.add((e, aurl[i]))
        except BaseException:
            pass
    #  print(ua)
    print("Found these episodes links:\n")
    links = sorted(list(links), key=lambda x: x[0])
    #  print(links)
    for e, l in links:
        print(e, l)
    browser.close()

s = input("Select episodes(e.g. 1,2,5-9 10 11):\n")
picked = set()
sl = re.split(r'; |, |\*|\n|,|;|\ ', s)
#  print(sl)
for i in sl:
    try:
        if '-' in i:
            [a, b] = list(map(int, i.split('-')))
            print(a, b)
            if (a > b):
                a, b = b, a
            for j in range(a, b + 1):
                picked.add(j)
        else:
            picked.add(int(i))
    except BaseException:
        print("Invalid episode", i)
        pass

for i in links:
    if i[0] in picked:
        print("Download", i[0], i[1])


#  from bs4 import BeautifulSoup
#  import requests
#  #  import pickle
#  #  import re
#  import sys
#
#  #  url = "http://duonaolive.com/detail?id=51848"
#  #  what = Beautiful things.
#  url = sys.argv[1]
#
#  reading = requests.get(url)
#
#  soup = BeautifulSoup(reading.text, "lxml")
#  #  trlist = soup.table.find_all('tr')
#  #  trlist = trlist[1:]
#  #  print([ _.text for _ in soup.find_all('h1')])
#  #  print([ _.text for _ in soup.find_all('a',href=True)])
#  season_title = soup.find_all('h1')[0].text
#
#  for a in soup.find_all('a', href=True):
#      t = a.text.replace('\n', '')
#      l = a['href']
#      if "../play" in l:
#          print(
#              l.replace("..", "http://duonaolive.com"),
#              (season_title + t).replace(" ", "")
#          )

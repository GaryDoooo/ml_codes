import sys
import asyncio
#  import re
from playwright.async_api import async_playwright
url = sys.argv[1]
#  print(url)

async def main():
    async with async_playwright() as p:
        #  browser = p.firefox.launch()
        browser = await p.chromium.launch(headless=False, slow_mo=100)

        page = await browser.new_page()
        print(url)
        await page.goto(url,
                  wait_until="networkidle", timeout=10000)
        #  ua = page.query_selector("01")
        atxt = await page.eval_on_selector_all(
            "a", "elements => elements.map(element => element.text)")
        aurl = await page.eval_on_selector_all(
            "a", "elements => elements.map(element => element.href)")
        hrefs = await page.evaluate("() => Array.from(document.querySelectorAll('a')).map(a => a.href)")
        print(hrefs)
        links = set()
        for i in range(len(atxt)):
            if "?id=" not in aurl[i]:
                continue
            if "play" not in aurl[i]:
                continue
            try:
                print(atxt[i], aurl[i])
                #  e = int(atxt[i].replace(' ', ''))
                #  print(e, aurl[i])
                links.add((atxt[i], aurl[i]))
            except BaseException:
                pass
        #  print(ua)
        #  print(links)
        print("Found these episodes links:\n")
        #  links = sorted(list(links), key=lambda x: x[0])
        #  print(links)
        for e, l in links:
            print(e, l)
        browser.close()

    for i in links:
        #  if i[0] in picked:
        print("Download", i[0], i[1])

asyncio.run(main())

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

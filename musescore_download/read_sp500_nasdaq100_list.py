from bs4 import BeautifulSoup
import requests
import pickle
import re

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
reading = requests.get(url)
soup = BeautifulSoup(reading.text, "lxml")
trlist = soup.table.find_all('tr')
trlist = trlist[1:]

sp500list = [str(_.td.string) for _ in trlist]
# the sp500 is listed in the first table on the page
# first row is not stock, the ticker names are in first col of each row

pickle.dump(sp500list, open("sp500list.p", 'wb'),
            protocol=0)  # protocol 0 is human readable

url = "https://en.wikipedia.org/wiki/NASDAQ-100"
reading = requests.get(url)
soup = BeautifulSoup(reading.text, "lxml")

lilist = soup.ol.find_all("li")  # the stock name list are in the only <ol>tag

tickerlist = [str(_.a.next_sibling) for _ in lilist]
# <li><a href="/wiki/Cintas" title="Cintas">Cintas Corporation</a> (CTAS)</li>
# an example above of the <li> tag contents
# this line gives the contents after </a> but inside </li>

tickerlist = [re.search("\([A-Z]+\)", _) for _ in tickerlist]
# search strings match all capital letters between two ( and )

tickerlist = [re.sub("\(|\)", "", _.group(0)) for _ in tickerlist]
# search function gives groups of answers, group(0) feedback the first one
# re.sub replace ( or ) into ""

pickle.dump(tickerlist, open("nasdaq100list.p", "wb"), protocol=0)

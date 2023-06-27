from bs4 import BeautifulSoup
import requests
import sys

url = sys.argv[1]

#  url = "https://www.khanacademy.org/science/ap-chemistry-beta/x2eef969c74e0d802:chemical-reactions"
#  what = Beautiful things.


def print_video_link(url):
    reading = requests.get(url)
    #  soup = BeautifulSoup(reading.text, "lxml")
    #  season_title = soup.find_all('h1')[0].text
    #  print(season_title)
    s = reading.text.split("\"")
    for l in [_.replace("\\", "")
              for _ in s if "youtube" in _ and _.endswith("mp4\\")]:
        print(l)


reading = requests.get(url)

soup = BeautifulSoup(reading.text, "lxml")
season_title = soup.find_all('h1')[0].text
print("##",season_title)

last = ""
for a in soup.find_all('a', href=True):
    t = a.text.replace('\n', '')
    l = a['href']
    if "science" in l and l != last and "/v/" in l:
        print("")
        print("###",l.split("/")[-1].replace("-", " "))
        print_video_link("https://www.khanacademy.org/" + l)
        last = l

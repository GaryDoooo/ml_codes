from bs4 import BeautifulSoup
import requests
import sys
url = sys.argv[1]

#  url = "https://www.khanacademy.org/science/ap-chemistry-beta/x2eef969c74e0d802:chemical-reactions/x2eef969c74e0d802:introduction-to-acid-base-reactions/v/bronsted-lowry-definition-of-acids-and-bases"

reading = requests.get(url)

soup = BeautifulSoup(reading.text, "lxml")
season_title = soup.find_all('h1')[0].text
print(season_title)
s = reading.text.split("\"")
for l in [_.replace("\\", "")
          for _ in s if "youtube" in _ and _.endswith("mp4\\")]:
    print(l)

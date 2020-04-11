from bs4 import BeautifulSoup
import re

with open('input.html', 'r') as file:
    data = file.read().replace('\n', '')

soup = BeautifulSoup(data, "lxml")

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))

from bs4 import BeautifulSoup
import requests

url = "https://musescore.com/hub/woodwinds/solo?instruments=29&page=1#main-content"
#  "https://musescore.com/hub/game-of-thrones?instruments=29&page=2"


def get_name_and_print_link(url_link):
    reading = requests.get(url_link)
    soup = BeautifulSoup(reading.text, "lxml")
    h2list = soup.find_all(
        'h2',
        {"class", "score-info__title"})
    linklist = [_.a["href"] for _ in h2list]
    print_link_list = [
        "https://musescore.com/score/print-parts/print-full?score_id="+_.split('/')[-1] for _ in linklist]
    name_list = [_.a.contents[0] for _ in h2list]
#  print(h2list[0].a.contents)
#  print(
#  "https://musescore.com/score/print-parts" +
#  "/print-full?score_id=" +
#  linklist[0].split('/')[-1])
# print(url.split("#")[0][:-1])
    return name_list, print_link_list


for page in range(1, 101):  # total 100 pages
    page_url = url.split("#")[0][:-1]+str(page)
    name_list, print_link_list = get_name_and_print_link(page_url)
    for (name, print_link) in zip(name_list, print_link_list):
        print(name, "\n", print_link)

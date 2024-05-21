from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.wsj.com/market-data/stocks"
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")  # this
chrome_options.add_argument("--disable-dev-shm-using")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=chrome_options)
driver.get(url)
sleep(1)
table_divs = driver.find_elements_by_tag_name("td") + driver.find_elements_by_tag_name("li") + driver.find_elements_by_tag_name(
    "p") + driver.find_elements_by_tag_name("div") + driver.find_elements_by_tag_name("table")
#  print(table_divs.get_text())
#  source = driver.page_source.encode('utf-8')
#  print(source)
exit(0)
print(len(table_divs))
for i in range(len(table_divs)):
    content = table_divs[i].get_attribute('innerHTML')
    if "Advancing" in content:
        advancing = table_divs[i + 1].get_attribute('innerHTML')
        NAZadvancing = table_divs[i + 2].get_attribute('innerHTML')
        print(advancing)
    if "Declining" in content:
        declining = table_divs[i + 1].get_attribute('innerHTML')
        NAZdeclining = table_divs[i + 2].get_attribute('innerHTML')
        print(declining)

table_divs = driver.find_elements_by_tag_name("span")
print(len(table_divs))
for i in range(len(table_divs)):
    content = table_divs[i].get_attribute('innerHTML')
    if "Markets Diary" in content:
        time = (table_divs[i + 1].get_attribute('innerHTML'))
        time = time[0:time.find("span") - 1] + ":" + \
            time[time.rfind("span") + 5:]

print("Time" + time, "NYSE A", advancing, "D", declining, end=" ")
advancing = int(advancing.replace(",", ""))
declining = int(declining.replace(",", ""))
print("Ratio %.3f" %
      (advancing / (advancing + declining)), end=" ")
print("NASDAQ A", NAZadvancing, "D", NAZdeclining, end=" ")
advancing = int(NAZadvancing.replace(",", ""))
declining = int(NAZdeclining.replace(",", ""))
print("Ratio %.3f" %
      (advancing / (advancing + declining)))


driver.close()

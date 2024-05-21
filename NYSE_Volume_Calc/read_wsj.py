from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#  import re

url = "https://www.wsj.com/market-data/stocks"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=chrome_options)
driver.get(url)


def wait_for_element(input_string):
    for _ in range(40):
        try:
            result = driver.find_element_by_xpath(input_string)
            #  print(_)
            return result
        except BaseException:
            sleep(0.5)
            pass
    #  print("Overtime 20 seconds")
    # add another
    return None


sleep(1)
table_divs = driver.find_elements_by_tag_name("td")
print(len(table_divs))
#  table_divs = driver.find_elements_by_class_name(
#  "WSJTables--table__body--3Y0p0d6H")
#  print(len(table_divs))
for i in range(len(table_divs)):
    #  td_class = _.get_content()
    content = table_divs[i].get_attribute('innerHTML')
    print(content)
    if "Advancing" in content:
        advancing = table_divs[i + 1].get_attribute('innerHTML')
        print(advancing)
    if "Declining" in content:
        declining = table_divs[i + 1].get_attribute('innerHTML')
        print(declining)

table_divs = driver.find_elements_by_tag_name("span")
print(len(table_divs))
for i in range(len(table_divs)):
    content = table_divs[i].get_attribute('innerHTML')
    if "Markets Diary" in content:
        time = (table_divs[i + 1].get_attribute('innerHTML'))
        #  print(time.find("span"), time.rfind("span"))
        time = time[0:time.find("span") - 1] + ":" + \
            time[time.rfind("span") + 5:]

print(time, "NYSE Advancing", advancing, "Declining", declining, end=" ")
advancing = int(advancing.replace(",", ""))
declining = int(declining.replace(",", ""))
print("Ratio %.2f" %
      (advancing / (advancing + declining)))

driver.close()

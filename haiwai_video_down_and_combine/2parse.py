from time import sleep
#  from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

page_url = "http://www.bilibili.com/mobile/video/av9069110.html"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=chrome_options)
url = "https://pv.vlogdownloader.com/"
#  "https://www.5tps.com/play/973_46_1_30.html"
#  "https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver"
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
    return None


#  sleep(1)

#  h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
#  audio = driver.find_element_by_xpath("//div[@id='full']").text
input_box = wait_for_element("//input[@id='url_input']")
if input_box is not None:
    input_box.send_keys(page_url)
#  submit_button = driver.find_element_by_xpath(
submit_button = wait_for_element("//button[@id='url_submit_button']")
if submit_button is not None:
    submit_button.click()
#  print(input_box, submit_button)
#  sleep(3)
result = wait_for_element("//input[@id='video0']")
#  print(result)
try:
    print(result.get_attribute("value"))
except BaseException:
    print("Element_Error")
#  print(result)
result = wait_for_element("//span[@class='text-danger']")
#  print(result)
try:
    print(re.sub(r'[\\/\:*"<>\|\.%\$\^&£]', '',
                 result.text.replace(" ", "")))
except BaseException:
    print("Element_Error")
#  print(result)

driver.close()

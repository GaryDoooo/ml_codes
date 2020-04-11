from time import sleep
#  from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=chrome_options)
url = "https://pv.vlogdownloader.com/"
#  "https://www.5tps.com/play/973_46_1_30.html"
#  "https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver"
driver.get(url)

sleep(1)

#  h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
#  audio = driver.find_element_by_xpath("//div[@id='full']").text
input_box = driver.find_element_by_xpath("//input[@id='url_input']")
#  print(input_box)
input_box.send_keys("https://www.bilibili.com/video/av83670203")
submit_button = driver.find_element_by_xpath(
    "//button[@id='url_submit_button']")
submit_button.click()

#  sleep(3)
result = driver.find_element_by_xpath("//input[@id='video0']")
#  print(result.get_attribute("value"))
#  print(result)
driver.close()

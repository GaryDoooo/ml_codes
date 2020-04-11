from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=chrome_options)
url = "https://www.5tps.com/play/973_46_1_30.html"
#  "https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver"
driver.get(url)

sleep(10)

#  h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
audio = driver.find_element_by_xpath("//div[@id='full']").text
print(audio)

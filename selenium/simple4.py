from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
url = "https://musescore.com/user/18154866/scores/4557796"
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
    return None
sleep(1)
allImages = driver.find_elements_by_tag_name("img")
for _ in allImages:
    imageurl = _.get_attribute("src")
    if imageurl is not None:
        if ".svg?" in imageurl:
            print(imageurl)
print(re.sub(r'[\\/\:*"<>\|\.%\$\^&£]', '',
             driver.title.split("|")[0]).replace(" ", "_"))
driver.close()

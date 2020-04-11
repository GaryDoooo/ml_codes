from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

url = "https://musescore.com/user/18154866/scores/4557796"
chrome_options = Options()
chrome_options.add_argument("--headless")
#  chrome_options.add_argument("--window-size=1366,5080")

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
#  first_image = driver.find_element_by_tag_name("img")
#  #  first_image.click()
#  #  first_image.send_keys(Keys.END)
#  actions = ActionChains(driver)
#  actions.move_to_element(first_image)
#  for _ in range(100):
#  actions.send_keys(Keys.DOWN)
#  actions.send_keys(Keys.RIGHT)
#  actions.perform()
#  sleep(0.1)
#
#
#  sleep(2)
#  allImages = driver.find_elements(By.TAG_NAME("img"))
allImages = driver.find_elements_by_tag_name("img")

#  print(allImages)
for _ in allImages:
    imageurl = _.get_attribute("src")
    if imageurl is not None:
        if ".svg?" in imageurl:
            print(imageurl)
#  print(driver.title)
print(re.sub(r'[\\/\:*"<>\|\.%\$\^&£]', '',
             driver.title.split("|")[0]).replace(" ", "_"))
#  from selenium.webdriver.common.keys import Keys
#  print(driver.find_element_by_tag_name("title"))

#  h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
#  audio = driver.find_element_by_xpath("//div[@id='full']").text
driver.close()

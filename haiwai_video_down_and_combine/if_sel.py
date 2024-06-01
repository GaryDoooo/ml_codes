from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  from selenium_firefox import Firefox
#
#  driver = Firefox()

from selenium.webdriver.chrome.options import Options
#
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-browser-side-navigation')

driver = webdriver.Chrome(options=chrome_options)
#  driver = webdriver.()
driver.get("https://www.iyf.tv/play/pbf7GYqCvg7?id=RXGQ9QgI7ID")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "__whole__"))
    )
    print(element)
finally:
    driver.quit()

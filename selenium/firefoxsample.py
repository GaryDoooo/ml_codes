from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#  from selenium.webdriver.chrome.options import Options


#  driver = webdriver.Chrome(executable_path="geckodriver")
#  "chromedriver", options=chrome_options)

driver = webdriver.Firefox(executable_path="geckodriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

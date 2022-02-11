from urllib.parse import urlparse
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import gzip
from os import environ


def get_resources(url: str) -> set:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-browser-side-navigation')

    resources = []
    #  driver.set_page_load_timeout(20)
    for i in range(5):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        sleep(5)

        # Access requests via the `requests` attribute
        for request in driver.requests:
            if request.response and urlparse(
                    url).netloc not in urlparse(request.url).netloc:
                resources.append(request.url)
                if ".m3u8" in request.url:
                    #  print(request.response.body)
                    #  print(request.url)
                    try:
                        c = request.response.body.decode("utf-8")
                    except BaseException:
                        c2 = gzip.decompress(request.response.body)
                        c = c2.decode('utf-8')
                    #  print(c)
                    if ".ts" in c:
                        #  o = urlparse(request.url)
                        print(request.url)
                        #  print(
                        #      o.scheme + "://" + o.netloc + "/" +
                        print([
                            _ for _ in c.split("\n") if ".ts" in _][0])
                        return

    return set(resources)


try:
    get_resources(environ.get('TESTARG'))
except BaseException:
    print("An exception occurred")

#  url = "https://www.tangrenjie.tv/vod/play/id/119053/sid/4/nid/7.html"
#  url = "https://www.baidu.com"
# url = "https://www.iyf.tv/watch?v=tZA37MHEha6bCoJ0dp5wy7"
#  url = "https://www.iyf.tv/play?id=S2vxMv8wt82"
#  s = get_resources(url)
#  print(s)
#  print([_ for _ in s if ".m3u8" in _])

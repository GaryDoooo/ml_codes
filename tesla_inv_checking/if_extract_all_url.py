from playwright.sync_api import sync_playwright
from time import sleep

url = 'https://www.tesla.com/inventory/new/my?TRIM=LRAWD&arrangeby=plh&zip=14534&range=0'

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    for i in range(10):
        try:
            page.goto(url,
                      wait_until="networkidle", timeout=30000)
            print(page.content())
            break
        except BaseException:
            sleep(30)
            pass

    browser.close()

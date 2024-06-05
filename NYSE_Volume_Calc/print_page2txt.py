import re
from playwright.sync_api import expect
from time import sleep
from playwright.sync_api import sync_playwright, Playwright
#  from playwright.async_api import async_playwright
#  import asyncio
#  from os import environ

url = 'https://www.wsj.com/market-data/stocks'


#  async def main(linkURL):
#      async with async_playwright() as p:
#          browser = await p.webkit.launch()
#          #  browser = await p.chromium.launch()
#          page = await browser.new_page()
#          try:
#              # , wait_until="networkidle", timeout=120000)
#              await page.goto(linkURL,timeout=120000)
#          except BaseException:
#              pass
#          print(await page.inner_text('div'))
#          await browser.close()
#
#
#  def main2(linkURL):
#      with sync_playwright() as p:
#          browser = p.webkit.launch()
#          #  browser = await p.chromium.launch()
#          page = browser.new_page()
#          page.goto(linkURL, wait_until="networkidle", timeout=120000)
#          print(page.inner_text('div'))
#          browser.close()


#  asyncio.run(main(environ.get('TESTARG')))
#  asyncio.run(main(url))
#  iterate_url(environ.get('TESTARG'))

def run(playwright: Playwright, url):
    #  iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(
        #  **iphone_13,
        locale='en-US'
    )
    page = context.new_page()
    page.goto(url)
    #  page.goto("https://www.iyf.tv/play/yYltcSemxw4?id=AYwLjKAcVK5")
    expect(page).to_have_title(re.compile("Stocks"))
    #  video = page.locator('#video_player')
    #  locator = page.get_by_role('video')
    #  expect(video).to_have_id('video_player')
    #  print(page.title())
    while True:
        text = page.inner_text('div')
        if "Diary" in text:
            print(text)
            break
        else:
            sleep(1)

    #  print(video.all_inner_texts())
    #  print(video.all_text_contents())
    #  print(video.evaluate("el => el.outerHTML"))
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright, url)

    #  main2(url)
    #  asyncio.run(main(url))

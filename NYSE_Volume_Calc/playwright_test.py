from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
#  from os import environ

url = "https://www.wsj.com/market-data/stocks"


def main2(linkURL):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        #  page.on("request", lambda request: print("Request: " + request.url))
        #  page.on(
        #      "response",
        #      lambda response: print(
        #          "Response: " +
        #          response.request.url))
        page.goto(linkURL)
        #  pageText = page.inner_text('')
        print(page.content())
        browser.close()


async def main(linkURL):
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        #  page.on("request", lambda request: print("Request: " + request.url))
        #  await page.goto("http://playwright.dev")
        #  await page.goto("https://www.iyf.tv/play?id=nmVPxY64z3F")
        await page.goto(linkURL)
        #  print(await page.content())
        print(await page.inner_text('div'))
        await browser.close()

#  <<<<<<< HEAD
#  main2(environ.get("TESTARG"))
#  =======
#  >>>>>>> 2fb1565caf279f56f0e6adb034a0c79f84c7dd86
asyncio.run(main(url))
#  asyncio.run(main2(url))
#  iterate_url(environ.get('TESTARG'))

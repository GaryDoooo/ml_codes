
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
from os import environ

with sync_playwright() as playwright:
    browser = playwright.webkit.launch()
    page = browser.new_page()
    page.on("request", lambda request: print("Request: " + request.url))
    page.on(
        "response",
        lambda response: print(
            "Response: " +
            response.request.url))
    #  page.setDefaultTimeout(10000)
    #  page.setDefaultNavigationTimeout(30000)
    page.goto("https://www.iyf.tv/play/SXCR45KNqi2")
    #  page.goto("https://www.iyf.tv/e072adb3-21cb-4db8-8101-e8681aa63507")
    #  page.goto("https://www.iyf.tv/1f313ff6-9ad4-4205-bab4-6d78c9185c6c")
    browser.close()


#  async def main(linkURL):
#      async with async_playwright() as p:
#          browser = await p.chromium.launch()
#          page = await browser.new_page()
#          page.on("request", lambda request: print("Request: " + request.url))
#          #  await page.goto("http://playwright.dev")
#          #  await page.goto("https://www.iyf.tv/play?id=nmVPxY64z3F")
#          await page.goto(linkURL)
#          print(await page.title())
#          await browser.close()
#
#  asyncio.run(main(environ.get("TESTARG")))

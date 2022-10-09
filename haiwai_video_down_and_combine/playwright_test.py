from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
from os import environ


def main2(linkURL):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.on("request", lambda request: print("Request: " + request.url))
        page.on(
            "response",
            lambda response: print(
                "Response: " +
                response.request.url))
        page.goto(linkURL)
        browser.close()


async def main(linkURL):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.on("request", lambda request: print("Request: " + request.url))
        #  await page.goto("http://playwright.dev")
        #  await page.goto("https://www.iyf.tv/play?id=nmVPxY64z3F")
        await page.goto(linkURL)
        print(await page.title())
        await browser.close()

asyncio.run(main(environ.get("TESTARG")))
#  iterate_url(environ.get('TESTARG'))

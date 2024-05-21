from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
#  from os import environ

url = 'https://www.wsj.com/market-data/stocks'


async def main(linkURL):
    async with async_playwright() as p:
        browser = await p.webkit.launch()
        #  browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            # , wait_until="networkidle", timeout=120000)
            await page.goto(linkURL,timeout=120000)
        except BaseException:
            pass
        print(await page.inner_text('div'))
        await browser.close()


def main2(linkURL):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        #  browser = await p.chromium.launch()
        page = browser.new_page()
        page.goto(linkURL, wait_until="networkidle", timeout=120000)
        print(page.inner_text('div'))
        browser.close()


#  asyncio.run(main(environ.get('TESTARG')))
#  asyncio.run(main(url))
#  iterate_url(environ.get('TESTARG'))
if __name__ == "__main__":
    #  main2(url)
    asyncio.run(main(url))

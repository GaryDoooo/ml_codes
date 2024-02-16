#  from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
from os import environ

url='https://www.tesla.com/inventory/new/my?TRIM=LRAWD&arrangeby=plh&zip=14534&range=0'

async def main(linkURL):
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        await page.goto(linkURL)
        #  print(await page.inner_text('div'))
        #  lease=page.locator('result-price-monthly-payment')
        print(await page.content())
        await browser.close()

#  asyncio.run(main(environ.get('TESTARG')))
asyncio.run(main(url))
#  iterate_url(environ.get('TESTARG'))

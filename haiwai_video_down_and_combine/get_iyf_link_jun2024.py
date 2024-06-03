import re
from playwright.sync_api import expect
from time import sleep
from playwright.sync_api import sync_playwright, Playwright
from os import environ


def run(playwright: Playwright, url):
    #  iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        #  **iphone_13,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto(url)
    #  page.goto("https://www.iyf.tv/play/yYltcSemxw4?id=AYwLjKAcVK5")
    sleep(2)
    expect(page).to_have_title(re.compile("爱壹帆"))
    video = page.locator('#video_player')
    #  locator = page.get_by_role('video')
    #  expect(video).to_have_id('video_player')
    print(page.title())
    print(video.all_inner_texts())
    print(video.all_text_contents())
    print(video.evaluate("el => el.outerHTML"))


with sync_playwright() as playwright:
    run(playwright, environ.get("TESTARG"))

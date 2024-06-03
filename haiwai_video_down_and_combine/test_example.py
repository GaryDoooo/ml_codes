import re
from playwright.sync_api import expect
from time import sleep
#
#
#  def test_has_title(page: Page):
#      page.goto("https://playwright.dev/")
#
#      # Expect a title "to contain" a substring.
#      expect(page).to_have_title(re.compile("Playwright"))
#
#
#  def test_get_started_link(page: Page):
#      page.goto("https://playwright.dev/")
#
#      # Click the get started link.
#      page.get_by_role("link", name="Get started").click()
#
#      # Expects page to have a heading with the name of Installation.
#      expect(page.get_by_role("heading", name="Installation")).to_be_visible()
#
#
#  def test_get_ify(page: Page):
#      page.goto("https://www.iyf.tv/play/yYltcSemxw4?id=AYwLjKAcVK5")
#      expect(page).to_have_title(re.compile("爱壹帆"))

from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    #  iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        #  **iphone_13,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto("https://www.iyf.tv/play/yYltcSemxw4?id=AYwLjKAcVK5")
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
    run(playwright)

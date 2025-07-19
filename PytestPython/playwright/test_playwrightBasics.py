
import pytest
from playwright.sync_api import Page
def test_playwrightBasics(playwright):
    browser=playwright.chromium.launch(headless=False) #By default playwright uses chromium in headless mode.headless=False opens the browser but for nightly run we will use headless as True
    context =  browser.new_context() #open new context every time , it gives seperate private browsing window
    page = context.new_page() #After opening the browser we need to open the page
    page.goto("https://playwright.dev/python/docs/intro#installing-playwright-pytest")


##page by default is implemented in Chromium engine in headless mode with single context
def test_playwrightShortCut(page:Page):
    page.goto("https://playwright.dev/python/docs/intro#installing-playwright-pytest")




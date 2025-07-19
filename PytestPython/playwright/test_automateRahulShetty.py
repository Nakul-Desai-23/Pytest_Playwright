import pytest
import time
from playwright.sync_api import Page, expect , Playwright


def test_corePlaywrightLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    time.sleep(2)
    page.get_by_label("username").fill("rahulshettyacademy")
    time.sleep(2)
    page.get_by_label("password").fill("learning")
    time.sleep(2)
    page.get_by_role("combobox").select_option("teach")
    time.sleep(2)
    page.locator("#terms").check()
    time.sleep(2)
    page.get_by_role("link",name="terms and conditions").click()
    time.sleep(2)
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(10)



def test_firefoxBrowser(playwright:Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning1234")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(10)


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("desai.nakul6603@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Apple@500")
    page.get_by_role("button", name="Login").click()
    page.locator("#sidebar div").filter(has_text=re.compile(r"^shoes$")).get_by_role("checkbox").check()
    page.locator("#sidebar div").filter(has_text=re.compile(r"^shoes$")).get_by_role("checkbox").uncheck()
    page.get_by_role("button", name=" Add To Cart").nth(1).click()
    page.get_by_role("button", name="   Cart").click()
    page.get_by_role("button", name="Checkout❯").click()
    page.locator(".user__address").click()
    page.get_by_role("textbox", name="Select Country").fill("India")
    page.locator(".ta-backdrop").click()
    page.locator("input[type=\"text\"]").nth(1).click()
    page.locator("input[type=\"text\"]").nth(1).fill("666")
    page.locator("input[type=\"text\"]").nth(2).click()
    page.locator("input[type=\"text\"]").nth(2).click()
    page.locator("input[type=\"text\"]").nth(2).fill("Nakul")
    page.get_by_role("listitem").filter(has_text="Sign Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)

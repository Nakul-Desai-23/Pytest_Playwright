from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    ##Create Order ---> Grab OrderID
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright)


    ##LOGIN
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("desai.nakul6603@gmail.com")
    page.locator("#userPassword").fill("Apple@500")
    page.get_by_role("button",name="login").click()

    ##Order History page ---> order is present
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()







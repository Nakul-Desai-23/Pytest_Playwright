import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


# -> api call from browser -> api call contact server return back response to the browser -> browser uses this response to create HTML report
def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=689481066f585eb60d6576bc")

def test_Network_2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.locator("#userEmail").fill("desai.nakul6603@gmail.com")
    page.locator("#userPassword").fill("Apple@500")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    ## Write script to inject token in session storage because all browsers renders in java script
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")  ##Here we are injecting java scriptn
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

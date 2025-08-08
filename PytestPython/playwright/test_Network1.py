from playwright.sync_api import Page

fakePayloadOrderResponse = {"message":"No Product in Cart"}
# -> api call from browser -> api call contact server return back response to the browser -> browser uses this response to create HTML report
def intercept_response(route):
    route.fulfill(
        json= fakePayloadOrderResponse
    )

def test_Network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.locator("#userEmail").fill("desai.nakul6603@gmail.com")
    page.locator("#userPassword").fill("Apple@500")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
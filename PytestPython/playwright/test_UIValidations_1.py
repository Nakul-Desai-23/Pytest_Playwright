import time

from playwright.sync_api import Page , expect


def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()
        child_page = newPage_info.value
        text = child_page.locator(".red").text_content()
        print(text) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at") # 0->Please email us 1-> mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"





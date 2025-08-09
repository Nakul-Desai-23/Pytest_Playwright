import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

##json file ----> util--->access into test

with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize("user_credentials" , user_credentials_list)
def test_e2e_web_api(playwright: Playwright ,user_credentials ):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    ##Create Order ---> Grab OrderID
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)

    ##LOGIN
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials['userEmail'])
    page.locator("#userPassword").fill(user_credentials['userPassword'])
    page.get_by_role("button", name="login").click()

    # ##Order History page ---> order is present
    page.get_by_role("button", name="ORDERS").click()
    page.wait_for_selector("table")
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
    # time.sleep(10)

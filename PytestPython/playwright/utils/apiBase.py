import json
import token

from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}

# 6896f7d66f585eb60d69e6e0
# 67a8df1ac0d3e6622a297ccb
class APIUtils:

    def getToken(self, playwright: Playwright,user_credentials):
        user_email  = user_credentials['userEmail']
        user_Password = user_credentials['userPassword']
        loginPayload = {"userEmail": user_email, "userPassword": user_Password}
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data=loginPayload)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def createOrder(self, playwright: Playwright,user_credentials):
        token = self.getToken(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data = json.dumps(ordersPayload),
                                            headers={"Authorization": token,
                                                     "content-type": "application/json"
                                                     })
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id


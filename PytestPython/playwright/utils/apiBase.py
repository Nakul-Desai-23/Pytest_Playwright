import token

from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}
loginPayload = {"userEmail": "desai.nakul6603@gmail.com", "userPassword": "Apple@500"}


class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data=loginPayload)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayload,
                                            headers={"Authorization": token,
                                                     "content-type": "application/json"
                                                     })
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id


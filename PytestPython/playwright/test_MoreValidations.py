import time

from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):

    ##Hide/Show Example and Placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alerts

    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()


    ##MOUSE HOVER
    page.locator("#mousehover").hover()

    page.get_by_role("link",name="Top").click()


    # ##HandlingFrames
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")


    # Check whether the price of RICE is 37
    # Identify the price column
    # Identify the rice row
    # Identify the price of rice


    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    ## Identify the price column
    for index in range (page.locator("th").count()):
       if page.locator("th").nth(index).filter(has_text="Price").count() > 0 :
           pricecolVal = index
           print(f"Price column value is  {pricecolVal}")
           break

    ## Identify the rice row
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(pricecolVal)).to_have_text("37")







import time

from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):

    ##Hide/Show Example and Placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    ##Alerts

    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()

    ##HandlingFrames
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

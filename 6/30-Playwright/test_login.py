from playwright.sync_api import Page, expect


def test_google_page(page: Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_url("https://www.google.com/")
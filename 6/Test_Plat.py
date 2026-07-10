from playwright.sync_api import Page, expect


def test_verify(page:Page):
    page.goto("https://u-njtarow.bemcorp.net/Accounts/Account/Account",timeout=60000)
    expect(page).to_have_url("https://u-njtarow.bemcorp.net/Accounts/Account/Account")

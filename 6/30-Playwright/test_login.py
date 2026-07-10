from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://u-njhtcp.bemcorp.net/Accounts/Account/Account",
        timeout=60000
    )

    expect(page).to_have_url(
        "https://u-njhtcp.bemcorp.net/Accounts/Account/Account"
    )
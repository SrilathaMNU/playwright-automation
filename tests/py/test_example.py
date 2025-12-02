import re
from playwright.sync_api import Page, expect

def test_homepage_has_playwright_in_title(page: Page) -> None:
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

def test_docs_page_can_be_opened(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Docs").click()
    expect(page).to_have_url(re.compile("docs"))
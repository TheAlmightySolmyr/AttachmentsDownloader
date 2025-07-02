from playwright.sync_api import sync_playwright

USER_DATA_DIR = "./chrome_profile"

def open_tab(url):
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            headless=False,
        )
        page = browser.new_page()
        page.goto(url)
        input('test')
        browser.close()


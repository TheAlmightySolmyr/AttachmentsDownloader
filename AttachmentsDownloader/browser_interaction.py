from playwright.sync_api import sync_playwright
from AttachmentsDownloader.url_former import form_url
import prompt


USER_DATA_DIR = "./user_data" 

def main(sheet_path):
    path = sheet_path
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            headless=False,
        )
        domain = prompt.string('input part of the url, if it required')
        page = browser.new_page()
        for i in form_url(path, 
                          domain):
            page.goto(i)
            input('test')
            page.close()
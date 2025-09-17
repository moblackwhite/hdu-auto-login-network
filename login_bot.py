import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv


def auto_login(url, username, password):
    with sync_playwright() as p:
        # 使用内置的 Chromium
        browser = p.chromium.launch(headless=False)  # False 表示显示浏览器
        page = browser.new_page()

        try:
            page.goto(url)
            page.wait_for_load_state("networkidle")

            page.fill("#username", username)
            page.fill("#password", password)
            page.click("#login-account")

            page.wait_for_timeout(5000)  # 等待登录完成
        except Exception as e:
            print(f"出错: {e}")
        finally:
            browser.close()

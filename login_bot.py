import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv


def auto_login(url, username, password, browser_type=None, headless=True):
    # 如果未指定浏览器，则根据系统自动选择：Linux 优先使用 firefox，其他默认 chromium
    if browser_type is None:
        if os.name == "posix" and "linux" in os.uname().sysname.lower():
            browser_type = "firefox"
        else:
            browser_type = "chromium"

    with sync_playwright() as p:
        # 动态选择浏览器
        if browser_type == "firefox":
            browser = p.firefox.launch(headless=headless)
        elif browser_type == "webkit":
            browser = p.webkit.launch(headless=headless)
        else:
            browser = p.chromium.launch(headless=headless)  # 默认使用 Chromium

        page = browser.new_page()

        try:
            page.goto(url)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(2000)

            page.fill("#username", username)
            page.wait_for_timeout(200)
            page.fill("#password", password)
            page.wait_for_timeout(200)
            page.click("#login-account")

            page.wait_for_timeout(5000)  # 等待登录完成
        except Exception as e:
            print(f"出错: {e}")
        finally:
            browser.close()

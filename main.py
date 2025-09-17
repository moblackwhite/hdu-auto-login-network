import os
from dotenv import load_dotenv
from login_bot import auto_login
from network_utils import is_connected_to_internet

if __name__ == "__main__":
    if not is_connected_to_internet():
        load_dotenv()
        url = "http://login.hdu.edu.cn/"
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        auto_login(url, username, password)
    else:
        print("当前有网络")

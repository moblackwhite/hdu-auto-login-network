import os
import time
import schedule
from dotenv import load_dotenv
from logger_config import setup_logger
from login_bot import auto_login
from network_utils import is_connected_to_internet

# 初始化日志
logger = setup_logger()

def check_network_and_login():
    """检查网络并尝试登录"""
    try:
        if is_connected_to_internet():
            logger.info("网络连接正常，无需登录。")
        else:
            logger.warning("检测到网络断开，正在尝试自动登录...")
            load_dotenv()  # 加载环境变量

            url = "http://login.hdu.edu.cn/"
            username = os.getenv("USERNAME")
            password = os.getenv("PASSWORD")

            if not username or not password:
                logger.error("未找到用户名或密码，请检查 .env 文件。")
                return

            try:
                auto_login(url, username, password)
                if is_connected_to_internet():
                    logger.info("自动登录成功！")
                else:
                    logger.error("自动登录失败，请检查账号或网络。")
            except Exception as e:
                logger.error(f"登录过程中发生异常: {e}")
    except Exception as e:
        logger.error(f"检查网络时发生未知错误: {e}")

if __name__ == "__main__":
    # 立即执行一次
    logger.info("=== 网络自动登录守护程序启动 ===")
    check_network_and_login()

    # 每 2 分钟执行一次
    schedule.every(2).minutes.do(check_network_and_login)

    logger.info("已设置定时任务：每 2 分钟检查一次网络状态...")

    # 保持程序运行
    while True:
        schedule.run_pending()
        time.sleep(1)
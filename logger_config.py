# logger_config.py
import logging
import os

def setup_logger():
    logger = logging.getLogger("NetworkLoginBot")
    logger.setLevel(logging.INFO)

    # 防止重复添加 handler
    if logger.handlers:
        return logger

    # 创建格式器
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 输出到文件
    file_handler = logging.FileHandler("bot.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # 输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
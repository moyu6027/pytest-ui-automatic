# -*- coding: utf-8 -*-
# @Author  : sean
# @File    : Log.py


import logging
import os
import time

logger = logging.getLogger("Pytest-UI-Automatic")
current_path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(current_path, "Log")
if os.path.exists(log_path):
    pass
else:
    os.mkdir(log_path, mode=0o777)


class LogInfo:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Log/log.log'
    err_file = path + '/Log/err.log'

    # 等级
    logger.setLevel(logging.DEBUG)
    # 格式
    formatter = '%(message)s - %(pathname)s[line:%(lineno)d]'

    # 两个handler用于写入不同文件
    info_handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')
    info_handler.setFormatter(logging.Formatter(formatter))
    err_handler.setFormatter(logging.Formatter(formatter))

    @staticmethod
    def info(message):
        logger.addHandler(LogInfo.info_handler)
        logger.info("[INFO " + get_current_time() + "]" + message)
        print(message)
        logger.removeHandler(LogInfo.info_handler)

    @staticmethod
    def error(message):
        logger.addHandler(LogInfo.err_handler)
        logger.error("[ERROR " + get_current_time() + "]" + message)
        print(message)
        logger.removeHandler(LogInfo.err_handler)

    @staticmethod
    def debug(message):
        logger.addHandler(LogInfo.info_handler)
        logger.debug("[DEBUG " + get_current_time() + "]" + message)
        print(message)
        logger.removeHandler(LogInfo.info_handler)

    @staticmethod
    def warning(message):
        logger.addHandler(LogInfo.info_handler)
        logger.warning("[WARNING " + get_current_time() + "]" + message)
        print(message)
        logger.removeHandler(LogInfo.info_handler)

    @staticmethod
    def critical(message):
        logger.addHandler(LogInfo.info_handler)
        logger.warning("[CRITICAL " + get_current_time() + "]" + message)
        logger.removeHandler(LogInfo.info_handler)
        print(message)


def get_current_time():
    date_format = '%Y-%m-%d %H:%M:%S'
    return time.strftime(date_format, time.localtime(time.time()))


if __name__ == "__main__":
    LogInfo.debug("This is debug message")
    LogInfo.info("This is info message")
    LogInfo.error("This is error")

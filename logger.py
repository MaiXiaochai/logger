# -*- coding: utf-8 -*-

"""
---------------------------------------
@File       : logger.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2020-07-09 11:28
@UpdatedOn  : 2020-11-04 16:18
---------------------------------------
"""

from os import makedirs
from os.path import basename, exists
from logging.handlers import RotatingFileHandler
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO


def log_handler(log_dir: str = None, filename: str = None, max_size: float = None, backup_count: int = None):
    """
    日志记录和打印
    :param log_dir:         保存日志的目录
    :param filename:        日志名称
    :param max_size:        单个日志文件最大大小，单位 MB
    :param backup_count:    备份日志的数量
    """
    # 默认值设置
    default_log_dir = '.'
    default_file_name = 'test'
    default_max_size = 10
    default_backup_count = 10

    # 处理参数值
    log_dir = log_dir or default_log_dir
    filename = filename or default_file_name
    max_size = max_size or default_max_size
    backup_count = backup_count or default_backup_count
    max_size = max_size * 1024 ** 2

    # 处理 log_file
    suffix = '.log'
    filename = filename if filename.endswith(suffix) else f"{filename}{suffix}"

    # 处理 log 文件保存目录的路径
    log_dir = log_dir.replace("\\", '/') if "\\" in log_dir else log_dir
    log_dir = log_dir if log_dir.endswith("/") else log_dir + '/'
    log_file_path = "{}{}".format(log_dir, filename)

    # log_dir 目录，如果不存在则创建
    if not exists(log_dir):
        makedirs(log_dir)

    # 日志行格式
    formatter = Formatter("[ %(asctime)s ][ %(levelname)s ][ %(filename)s:%(funcName)s:%(lineno)d ][ %(message)s ]")

    stream_handler = StreamHandler()
    stream_handler.setLevel(DEBUG)
    stream_handler.setFormatter(formatter)

    rotating_file_handler = RotatingFileHandler(
        filename=log_file_path, maxBytes=max_size, backupCount=backup_count, encoding="utf-8")

    # ≥ INFO级别才记录到文件
    rotating_file_handler.setLevel(INFO)
    rotating_file_handler.setFormatter(formatter)

    logger = getLogger(basename(__file__))
    logger.setLevel(DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(rotating_file_handler)

    return logger

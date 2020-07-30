# -*- coding: utf-8 -*-

"""
---------------------------------------
@File       : logger.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2020/7/9 11:28
---------------------------------------
"""

from os.path import basename
from logging.handlers import RotatingFileHandler
from logging import getLogger, StreamHandler, Formatter, DEBUG

from .conf_parser import config


def __logger():
    cfg = config()
    logger = getLogger(basename(__file__))

    # log 文件路径设置
    log_file_name = cfg.get('log_file_name')
    log_dir = cfg.get('log_dir')
    log_number = int(cfg['log_number'])
    log_size = float(cfg['log_size']) * 1024 ** 2

    log_dir = log_dir if log_dir.endswith("/") else log_dir + '/'
    log_file_path = f"{log_dir}{log_file_name}"

    handler1 = StreamHandler()
    handler2 = RotatingFileHandler(filename=log_file_path, maxBytes=log_size, backupCount=log_number, encoding="utf-8")

    logger.setLevel(DEBUG)
    handler1.setLevel(DEBUG)
    handler2.setLevel(DEBUG)

    formatter = Formatter("[ %(asctime)s ][ %(levelname)s ][ %(filename)s:%(funcName)s ][ %(message)s ]")
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger.addHandler(handler1)
    logger.addHandler(handler2)

    return logger


log = __logger()

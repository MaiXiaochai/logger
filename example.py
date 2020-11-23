# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : example.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2020/11/23 22:10
--------------------------------------
"""
from logger import log_handler


def demo():
    """
    test.log:
        [ 2020-11-23 22:16:00,740 ][ INFO ][ example.py:demo:18 ][ 0 ]
        [ 2020-11-23 22:16:00,741 ][ INFO ][ example.py:demo:18 ][ 1 ]
        [ 2020-11-23 22:16:00,741 ][ INFO ][ example.py:demo:18 ][ 2 ]
    """
    log = log_handler()

    for i in range(3):
        log.info(i)


if __name__ == '__main__':
    demo()

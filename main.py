'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-02-24 16:33:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import pyautogui
import logging
import tool
import home_reg
import time
import transfer

logging.basicConfig(level=logging.DEBUG)

t = transfer.StatusControlThread()
t.start()

try:
    while True:
        logging.info('STATUS_MAIN')
        t.set_target_status('STATUS_MAIN')
        time.sleep(5)
        print(t)
        logging.info('STATUS_MAIN_PVP')
        t.set_target_status('STATUS_MAIN_PVP')
        time.sleep(5)
        print(t)
# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    t.stop()
    print('已退出')

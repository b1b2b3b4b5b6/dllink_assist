'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-02-25 21:57:33
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
t.set_target_status('STATUS_TRANSDOOR_DUEL')

try:
    while True:
        time.sleep(10)
        print(t)
except KeyboardInterrupt:
    t.stop()
    print('已退出')

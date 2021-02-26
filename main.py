'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-02-27 00:02:09
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


def npc(control):
    control.goto_status('STATUS_MAIN', 0)
    tool.Operation(tool.Operation.CLICK, [[269, 560]]).action()
    time.sleep(0.5)
    tool.Operation(tool.Operation.CLICK, [[269, 680]]).action()
    time.sleep(0.5)

    control.goto_status('STATUS_MAIN_PVP', 0)
    tool.Operation(tool.Operation.CLICK, [[270, 553]]).action()
    time.sleep(0.5)
    tool.Operation(tool.Operation.CLICK, [[269, 609]]).action()
    time.sleep(0.5)
    tool.Operation(tool.Operation.CLICK, [[339, 600]]).action()
    time.sleep(0.5)

    control.goto_status('STATUS_MAIN_STORE', 0)
    tool.Operation(tool.Operation.CLICK, [[270, 663]]).action()
    time.sleep(0.5)
    tool.Operation(tool.Operation.CLICK, [[270, 762]]).action()
    time.sleep(0.5)
    tool.Operation(tool.Operation.CLICK, [[270, 591]]).action()
    time.sleep(0.5)


logging.basicConfig(level=logging.DEBUG)

t = transfer.StatusControlThread()
t.start()
t.set_target_status('STATUS_MAIN')

try:
    while True:
        npc(t)
except KeyboardInterrupt:
    t.stop()
    print('已退出')

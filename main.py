'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-02-27 21:11:47
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
    tool.Operation(tool.Operation.CLICK, [[269, 590]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 610]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 630]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 650]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 670]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 690]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 710]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[315, 673]]).action()
    time.sleep(0.1)

    tool.Operation(tool.Operation.CLICK, [[214, 590]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[338, 590]]).action()
    time.sleep(0.1)

    control.goto_status('STATUS_MAIN_PVP', 0)
    tool.Operation(tool.Operation.CLICK, [[270, 553]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 609]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[339, 600]]).action()
    time.sleep(0.1)

    control.goto_status('STATUS_MAIN_STORE', 0)
    tool.Operation(tool.Operation.CLICK, [[270, 663]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[270, 762]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[270, 591]]).action()
    time.sleep(0.1)


logging.basicConfig(level=logging.INFO)

t = transfer.StatusControlThread()
t.start()
t.goto_status('STATUS_MAIN')

try:
    while True:
        npc(t)
        t.goto_status('STATUS_PVP_DUEL')
        t.goto_status('STATUS_MAIN')

except KeyboardInterrupt:
    t.stop()
    print('已退出')

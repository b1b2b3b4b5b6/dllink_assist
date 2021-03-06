'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-03-07 02:13:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import pyautogui
import logging
import tool
import time
import transfer
import schedule
import collections


def pvp(control):
    logging.info('do pvp start')
    control.goto_status('STATUS_PVP_DUEL', 0)
    control.goto_status('STATUS_PVP_PREPARE', 0)
    logging.info('do pvp stop')


def npc(control):
    logging.info('do npc start')
    control.goto_status('STATUS_GATE_SEL', 0)
    tool.Operation(tool.Operation.CLICK, [[269, 573]]).action()
    time.sleep(0.1)
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
    tool.Operation(tool.Operation.CLICK, [[209, 674]]).action()
    time.sleep(0.1)

    control.goto_status('STATUS_PVP_SEL', 0)
    tool.Operation(tool.Operation.CLICK, [[270, 553]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[269, 609]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[339, 600]]).action()
    time.sleep(0.1)
    tool.Operation(tool.Operation.CLICK, [[287, 524]]).action()
    time.sleep(0.1)

    control.goto_status('STATUS_GATE_SEL', 0)
    logging.info('do npc stop')


logging.basicConfig(level=logging.INFO)

t = transfer.StatusControlThread()
t.start()

schedule.every().hour.do(npc, t)
schedule.every(3).seconds.do(pvp, t)
schedule.run_all()

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    t.stop()
    print('已退出')

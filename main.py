'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2022-01-05 21:45:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import logging
import time
import transfer
import schedule
import tool

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')


def pvp(control: transfer.StatusControlThread):
    logging.info('do pvp start')
    control.goto_status('STATUS_PVP_ING', 0)
    control.set_thread_status('pause')
    tool.OperationRightClick([580, -14], delay=30).action()
    tool.OperationLeftClick([560, -14], delay=5).action()
    control.set_target_status('STATUS_PVP_PREPARE')
    control.set_thread_status('run')
    control.wait_for_status('STATUS_NEXT', 15)

    logging.info('do pvp finished')


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


tool.init()
t = transfer.StatusControlThread()
t.start()

schedule.every(20).minutes.do(npc, t)
schedule.every(3).seconds.do(pvp, t)
schedule.run_all()

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    t.set_thead_status('stop')
    print('已退出')

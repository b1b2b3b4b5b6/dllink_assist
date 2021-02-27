'''
Author: your name
Date: 2021-02-25 20:25:40
LastEditTime: 2021-02-27 23:55:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\duel.py
'''

import tool
import time
import logging


def get_status():
    tool.capture_screenshot()
    if tool.find_img(tool.get_app_screenshot(), 'img/duel/your_action_turn.png') != None:
        return 'ACTION'

    if tool.find_img(tool.get_app_screenshot(), 'img/duel/continue_attack.png') != None:
        tool.Operation(tool.Operation.CLICK, [[381, 524]]).action()
        return 'BATTLE'
    if tool.find_img(tool.get_app_screenshot(), 'img/duel/your_battle_turn.png') != None:
        return 'BATTLE'
    if tool.find_img(tool.get_app_screenshot(), 'img/duel/record.png') != None:
        return 'COMPLETE'

    if tool.check_lose_connect() == True:
        return 'COMPLETE'

    for i in range(3):
        refresh()
        time.sleep(0.3)


def refresh():
    double_click([9, 482], 200)


def double_click(xy, dur=400):
    tool.Operation(tool.Operation.CLICK, [xy]).action()
    time.sleep(dur / 1000)

    tool.Operation(tool.Operation.CLICK, [xy]).action()
    time.sleep(dur / 1000)


def reset_sight():
    time.sleep(0.5)
    double_click([9, 482], 100)
    time.sleep(1)


def call():
    logging.debug('select monster')
    tool.Operation(tool.Operation.SLIDE, [[202, 913], [260, 563]]).action()

    time.sleep(0.4)

    logging.debug('call monster')
    tool.Operation(tool.Operation.CLICK, [[209, 728]]).action()

    time.sleep(2)
    logging.debug('enter battle')
    double_click([510, 630], 1000)


def battle():
    logging.debug('attack 1')
    reset_sight()
    tool.Operation(tool.Operation.SLIDE, [[160, 556], [281, 358]]).action()
    time.sleep(2)

    logging.debug('attack 2')
    reset_sight()
    tool.Operation(tool.Operation.SLIDE, [[274, 553], [281, 358]]).action()
    refresh()
    time.sleep(2)

    logging.debug('attack 3')
    reset_sight()
    tool.Operation(tool.Operation.SLIDE, [[382, 553], [281, 358]]).action()
    refresh()
    time.sleep(2)

    logging.debug('end turn')
    double_click([510, 630], 800)


def run_loop(status):
    logging.info(f'enter duel mode[{status}]')
    if status == 'STATUS_TRANSDOOR_DUEL':
        while True:
            if get_status() == 'ACTION':
                call()
                continue
            if get_status() == 'BATTLE':
                battle()
                continue
            if get_status() == 'COMPLETE':
                break

    if status == 'STATUS_PVP_DUEL':
        tool.Internet().reboot(12)
        time.sleep(65)

        return None
        while True:
            if get_status() == 'ACTION':
                call()
                continue
            if get_status() == 'BATTLE':
                logging.debug('end turn')
                double_click([510, 630], 800)
                continue
            if get_status() == 'COMPLETE':
                break
    logging.info('exit duel mode')

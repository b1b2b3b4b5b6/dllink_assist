'''
Author: your name
Date: 2021-02-25 20:25:40
LastEditTime: 2021-02-25 21:57:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\duel.py
'''

import tool
import time
import logging


def get_status():
    tool.capture_screenshot()
    if tool.find_img(tool.get_screenshot(), 'img/duel/your_action_turn.png') != None:
        return 'ACTION'
    if tool.find_img(tool.get_screenshot(), 'img/duel/your_battle_turn.png') != None:
        return 'BATTLE'

    if tool.find_img(tool.get_screenshot(), 'img/duel/save_replay.png') != None and tool.find_img(tool.get_screenshot(), 'img/duel/record.png') != None:
        return 'COMPLETE'

    for i in range(3):
        refresh()
        time.sleep(0.3)


def refresh():
    ope = tool.Operation(tool.Operation.CLICK, [[9, 482]])
    ope.action()


def reset_sight():
    ope = tool.Operation(tool.Operation.CLICK, [[9, 482]])
    ope.action()
    ope = tool.Operation(tool.Operation.CLICK, [[9, 482]])
    ope.action()
    time.sleep(1)


def call():
    logging.debug('select monster')
    ope = tool.Operation(tool.Operation.SLIDE, [[202, 913], [260, 563]])
    ope.action()
    time.sleep(1)

    logging.debug('call monster')
    ope = tool.Operation(tool.Operation.CLICK, [[209, 728]])
    ope.action()
    time.sleep(3)

    logging.debug('enter battle')
    ope = tool.Operation(tool.Operation.CLICK, [[510, 630]])
    ope.action()
    time.sleep(0.5)
    ope = tool.Operation(tool.Operation.CLICK, [[510, 630]])
    ope.action()
    time.sleep(0.5)


def battle():
    logging.debug('attack 1')
    reset_sight()
    ope = tool.Operation(tool.Operation.SLIDE, [[160, 556], [281, 358]])
    ope.action()
    time.sleep(2)

    logging.debug('attack 2')
    reset_sight()
    ope = tool.Operation(tool.Operation.SLIDE, [[274, 553], [281, 358]])
    ope.action()
    time.sleep(2)

    logging.debug('attack 3')
    reset_sight()
    ope = tool.Operation(tool.Operation.SLIDE, [[382, 553], [281, 358]])
    ope.action()
    time.sleep(2)

    logging.debug('end turn')
    ope = tool.Operation(tool.Operation.CLICK, [[510, 630]])
    ope.action()
    time.sleep(0.5)
    ope = tool.Operation(tool.Operation.CLICK, [[510, 630]])
    ope.action()
    time.sleep(0.5)


def loop():
    logging.info('enter duel mode')
    while True:
        if get_status() == 'ACTION':
            call()
            continue
        if get_status() == 'BATTLE':
            battle()
            continue
        if get_status() == 'COMPLETE':
            break
    logging.info('exit duel mode')

'''
Author: your name
Date: 2021-02-22 15:42:01
LastEditTime: 2021-02-22 16:59:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\global_reg.py
'''
import tool
import logging

CLOSE_JUMP_INFO = 'CLOSE_JUMP_INFO'

STATUS_JUMP_INFO = 'STATUS_JUMP_INFO'
CLOSE_JUMP_RECONNECT = 'CLOSE_JUMP_RECONNECT'

STATUS_JUMP_RECONNECT = 'STATUS_JUMP_RECONNECT'

jump_list = [
    {
        'img': 'img/home/jump_reconnect.png',
        'ope_name': CLOSE_JUMP_RECONNECT,
        'act_name': tool.Operation.CLICK,
        'status': STATUS_JUMP_RECONNECT
    }
]

jump_list = [
    {
        'img': 'img/home/jump_close.png',
        'ope_name': CLOSE_JUMP_INFO,
        'act_name': tool.Operation.CLICK,
        'status': STATUS_JUMP_INFO
    },

    {
        'img': 'img/home/jump_ok.png',
        'ope_name': CLOSE_JUMP_INFO,
        'act_name': tool.Operation.CLICK,
        'status': STATUS_JUMP_INFO
    }
]

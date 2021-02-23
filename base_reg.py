'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2021-02-24 03:52:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool

HANDLE_REFRESH = 'HANDLE_REFRESH'


class STATUS_BASE:

    def __init__(self):
        self.source_list = []
        self.transfer_list = []
        self.handle_list = [
            {
                'ope_name': 'HANDLE_REFRESH',
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        ]


class JUMP_BASE:
    def __init__(self):
        self.staimg_list = [
            {
                "STATUS":}
        ]

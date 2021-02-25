'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2021-02-25 21:21:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
from dict_recursive_update import recursive_update

HANDLE_REFRESH = 'HANDLE_REFRESH'


class STATUS_BASE:

    def __init__(self):
        self.transfer_dict = {}
        self.handle_dict = {}
        self.staimg_list = {}


class STATUS_LOSSCONNECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [387, 551]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/loss_connect.png'
        ]


class STATUS_DIALOGBOX(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [508, 676]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/skip.png'
        ]


class STATUS_REPORT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [41, 950]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/report.png'
        ]

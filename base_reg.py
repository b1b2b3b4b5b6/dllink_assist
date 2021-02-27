'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2021-02-27 22:40:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
from dict_recursive_update import recursive_update


class STATUS_BASE:
    PRI_HIGH = 10
    PRI_MID = 5
    PRI_LOW = 0

    def __init__(self):
        self.priority = self.PRI_MID
        self.transfer_dict = {}
        self.handle_dict = {}
        self.staimg_list = {}


class STATUS_LOSSCONNECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [380, 536]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/loss_connect.png'
        ]

        self.priority = self.PRI_LOW


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

        self.priority = self.PRI_LOW


class STATUS_START_GAME(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [264, 596]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/start_game.png'
        ]

        self.priority = self.PRI_LOW


class STATUS_REPORT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [44, 930]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/report.png'
        ]

        self.priority = self.PRI_LOW


class STATUS_GOOD(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/main/good.png'
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/good.png'
        ]

        self.priority = self.PRI_LOW


class STATUS_NEXT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/main/next_step.png'
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/next_step.png'
        ]

        self.priority = self.PRI_LOW


class STATUS_CLOSE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/main/close.png'
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/close.png'
        ]

        self.priority = self.PRI_LOW


class STATUS_SERVER_ERROR(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [269, 542]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/server_error.png'
        ]

        self.priority = self.PRI_LOW


class STATUS_CONNECT_ERROR(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [269, 542]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/main/connect_error.png'
        ]

        self.priority = self.PRI_HIGH

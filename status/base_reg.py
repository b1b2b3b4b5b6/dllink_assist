'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2021-03-07 02:52:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
from dict_recursive_update import recursive_update


class STATUS_BASE:
    PRI_TOP = float('inf')
    PRI_HIGH = 10
    PRI_MID = 5
    PRI_LOW = 0
    PRI_BOTTOM = -float('inf')

    def __init__(self):
        self.priority = self.PRI_MID
        self.transfer_dict = {}
        self.handle_dict = {}
        self.staimg_list = {
            'yes': [],
            'no': []
        }


class STATUS_LOSS_CONNECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE': {
                'act_name': tool.Operation.CLICK,
                'xy': [380, 536]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/loss_connect.png'],
            'no': []
        }

        self.priority = self.PRI_TOP


class STATUS_DAILY_INFO(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [508, 676]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/skip.png'],
            'no': []

        }

        self.priority = self.PRI_TOP


class STATUS_START_GAME(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [264, 596]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/start_game.png'],
            'no': []

        }

        self.priority = self.PRI_TOP


class STATUS_REPORT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [44, 930]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/report.png'],
            'no': []

        }

        self.priority = self.PRI_HIGH


class STATUS_GOOD(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/base/ok.png'
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/ok.png'],
            'no': []

        }

        self.priority = self.PRI_TOP


class STATUS_NEXT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/base/next_step.png'
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/next_step.png'],
            'no': []

        }

        self.priority = self.PRI_HIGH


class STATUS_CLOSE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/base/close.png'
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/close.png'],
            'no': []

        }

        self.priority = self.PRI_LOW


class STATUS_SERVER_ERROR(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [269, 542]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/server_error.png'],
            'no': []

        }

        self.priority = self.PRI_TOP


class STATUS_CONNECT_ERROR(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [269, 542]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/base/connect_error.png'],
            'no': []

        }

        self.priority = self.PRI_TOP

'''
Author: your name
Date: 2021-03-04 21:33:52
LastEditTime: 2021-03-07 03:26:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\pvp_reg.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_PVP_SEL(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [91, 920]
            },
            'STATUS_PVP_HOME': {
                'act_name': tool.Operation.CLICK,
                'xy': [209, 932]
            },
            'STATUS_STORE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [336, 930]
            },
            'STATUS_WORK_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [452, 926]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/pvp/sel.png'],
            'no': []

        }


class STATUS_PVP_HOME(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_PVP_PREPARE': {
                'act_name': tool.Operation.CLICK_ON_IMG,
                'img': 'img/home/pvp/click_to_prepare.png'
            },
            'STATUS_PVP_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [41, 928]
            }
        }

        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/pvp/home.png'],
            'no': []

        }


class STATUS_PVP_PREPARE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_PVP_DUEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [266, 428]
            },
            'STATUS_PVP_HOME': {
                'act_name': tool.Operation.CLICK,
                'xy': [41, 928]
            }
        }

        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/pvp/prepare.png'],
            'no': []

        }


class STATUS_NICE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_SEND_NICE': {
                'act_name': tool.Operation.CLICK,
                'xy': [59, 863]
            }
        }

        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/pvp/nice.png'],
            'no': []

        }


class STATUS_SEND_NICE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_PVP_PREPARE': {
                'act_name': tool.Operation.CLICK,
                'xy': [377, 536]
            }
        }

        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/pvp/send_nice.png'],
            'no': []

        }

        self.priority = self.PRI_HIGH

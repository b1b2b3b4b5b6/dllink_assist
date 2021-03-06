'''
Author: your name
Date: 2021-03-04 21:31:46
LastEditTime: 2021-03-07 03:22:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\trans_door.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_GATE_SEL(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_10': {
                'act_name': tool.Operation.CLICK,
                'xy': [91, 920]
            },
            'STATUS_PVP_SEL': {
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
            'yes': ['img/home/gate/sel.png'],
            'no': []

        }


class STATUS_GATE_10(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_PREPARE': {
                'act_name': tool.Operation.CLICK,
                'xy': [277, 834]
            },
            'STATUS_GATE_10': {
                'act_name': tool.Operation.CLICK,
                'xy': [89, 664]
            },
            'STATUS_GATE_20': {
                'act_name': tool.Operation.CLICK,
                'xy': [202, 664]
            },
            'STATUS_GATE_30': {
                'act_name': tool.Operation.CLICK,
                'xy': [322, 664]
            },
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [46, 934]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/gate/switch.png',
                    'img/home/gate/level_10.png'],
            'no': []

        }


class STATUS_GATE_20(STATUS_GATE_10):
    def __init__(self):
        super().__init__()
        self.transfer_dict.pop('STATUS_GATE_PREPARE')
        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = {
            'yes': [
                'img/home/gate/switch.png',
                'img/home/gate/level_20.png'
            ],
            'no': []
        }


class STATUS_GATE_30(STATUS_GATE_10):
    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_GATE_PREPARE')
        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/gate/switch.png',
                    'img/home/gate/level_30.png'],
            'no': []

        }


class STATUS_GATE_PREPARE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_DUEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [310, 834]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/gate/prepare.png'],
            'no': []

        }

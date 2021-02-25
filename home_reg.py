'''
Author: your name
Date: 2021-02-21 23:54:10
LastEditTime: 2021-02-26 00:32:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\detect.py
'''


import tool
import logging
from base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_MAIN(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_TRANSDOOR_10': {
                'act_name': tool.Operation.CLICK,
                'xy': [91, 920]
            },
            'STATUS_MAIN_PVP': {
                'act_name': tool.Operation.CLICK,
                'xy': [209, 932]
            },
            'STATUS_MAIN_STORE': {
                'act_name': tool.Operation.CLICK,
                'xy': [336, 930]
            },
            'STATUS_MAIN_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [452, 926]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main.png'
        ]


class STATUS_MAIN_PVP(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR_10')
        self.transfer_dict.pop('STATUS_MAIN_PVP')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [91, 920]
            },
            'STATUS_PVP': {
                'act_name': tool.Operation.CLICK,
                'xy': [209, 932]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main_pvp.png'
        ]


class STATUS_MAIN_STORE(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR_10')
        self.transfer_dict.pop('STATUS_MAIN_STORE')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [91, 920]
            },
            'STATUS_STORE': {
                'act_name': tool.Operation.CLICK,
                'xy': [336, 930]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main_store.png'
        ]


class STATUS_MAIN_WORK(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR_10')
        self.transfer_dict.pop('STATUS_MAIN_WORK')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [91, 920]
            },
            'STATUS_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [452, 926]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main_work.png'
        ]


class STATUS_TRANSDOOR_10(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_ONE_WORD': {
                'act_name': tool.Operation.CLICK,
                'xy': [277, 834]
            },
            'STATUS_TRANSDOOR_10': {
                'act_name': tool.Operation.CLICK,
                'xy': [89, 664]
            },
            'STATUS_TRANSDOOR_20': {
                'act_name': tool.Operation.CLICK,
                'xy': [202, 664]
            },
            'STATUS_TRANSDOOR_30': {
                'act_name': tool.Operation.CLICK,
                'xy': [322, 664]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/trans_door/switch_door.png',
            'img/trans_door/level_10.png'
        ]


class STATUS_TRANSDOOR_20(STATUS_TRANSDOOR_10):
    def __init__(self):
        super().__init__()
        self.transfer_dict.pop('STATUS_ONE_WORD')
        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/trans_door/switch_door.png',
            'img/trans_door/level_20.png'
        ]


class STATUS_TRANSDOOR_30(STATUS_TRANSDOOR_10):
    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_ONE_WORD')
        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/trans_door/switch_door.png',
            'img/trans_door/level_30.png'
        ]


class STATUS_ONE_WORD(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_TRANSDOOR_PREPARE': {
                'act_name': tool.Operation.CLICK,
                'xy': [277, 855]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/duel/oneword.png'
        ]


class STATUS_TRANSDOOR_PREPARE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_TRANSDOOR_DUEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [277, 834]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/trans_door/prepare.png'
        ]


class STATUS_TRANSDOOR_DUEL(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
        }
        recursive_update(self.transfer_dict, custom_dict)
        self.staimg_list = [
            'img/duel/npc_handle_pvp_1.png',
            'img/duel/npc_handle_pvp_2.png',
            'img/duel/select.png'
        ]


class STATUS_TRANSDOOR_DUEL_COMPLETE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_TRANSDOOR_DUEL_RESULT': {
                'act_name': tool.Operation.CLICK,
                'xy': [265, 913]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/duel/record.png'
        ]


class STATUS_TRANSDOOR_DUEL_RESULT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [265, 913]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/duel/duel_result.png'
        ]

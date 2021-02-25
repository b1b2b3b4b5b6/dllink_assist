'''
Author: your name
Date: 2021-02-21 23:54:10
LastEditTime: 2021-02-25 21:51:57
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
            'STATUS_TRANSDOOR': {
                'act_name': tool.Operation.CLICK,
                'xy': [102, 944]
            },
            'STATUS_MAIN_PVP': {
                'act_name': tool.Operation.CLICK,
                'xy': [229, 948]
            },
            'STATUS_MAIN_STORE': {
                'act_name': tool.Operation.CLICK,
                'xy': [340, 953]
            },
            'STATUS_MAIN_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [480, 953]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main.png'
        ]


class STATUS_MAIN_PVP(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR')
        self.transfer_dict.pop('STATUS_MAIN_PVP')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [102, 944]
            },
            'STATUS_PVP': {
                'act_name': tool.Operation.CLICK,
                'xy': [229, 948]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main_pvp.png'
        ]


class STATUS_MAIN_STORE(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR')
        self.transfer_dict.pop('STATUS_MAIN_STORE')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [102, 944]
            },
            'STATUS_STORE': {
                'act_name': tool.Operation.CLICK,
                'xy': [340, 953]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main_store.png'
        ]


class STATUS_MAIN_WORK(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR')
        self.transfer_dict.pop('STATUS_MAIN_WORK')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [102, 944]
            },
            'STATUS_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [480, 953]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/home/main_work.png'
        ]


class STATUS_TRANSDOOR(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_ONE_WORD': {
                'act_name': tool.Operation.CLICK,
                'xy': [277, 855]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/trans_door/switch_door.png'
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
                'xy': [277, 855]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = [
            'img/trans_door/prepare_10.png'
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
                'xy': [274, 934]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/duel/save_replay.png',
            'img/duel/record.png'
        ]


class STATUS_TRANSDOOR_DUEL_RESULT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [284, 934]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            'img/duel/duel_result.png'
        ]

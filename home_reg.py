'''
Author: your name
Date: 2021-02-21 23:54:10
LastEditTime: 2021-02-24 06:27:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\detect.py
'''


import tool
import logging
import except_reg
from base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_MAIN(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_TRANSDOOR': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            'STATUS_MAIN_PVP': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            'STATUS_MAIN_STORE': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            'STATUS_MAIN_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.staimg_dict, custom_dict)


class STATUS_MAIN_PVP(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR')
        self.transfer_dict.pop('STATUS_MAIN_PVP')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            'STATUS_PVP': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.staimg_dict, custom_dict)


class STATUS_MAIN_STORE(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR')
        self.transfer_dict.pop('STATUS_MAIN_STORE')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            'STATUS_STORE': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.staimg_dict, custom_dict)


class STATUS_MAIN_WORK(STATUS_MAIN):

    def __init__(self):
        super().__init__()

        self.transfer_dict.pop('STATUS_TRANSDOOR')
        self.transfer_dict.pop('STATUS_MAIN_WORK')
        custom_dict = {
            'STATUS_MAIN': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            'STATUS_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.staimg_dict, custom_dict)

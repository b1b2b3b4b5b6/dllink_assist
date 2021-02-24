'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2021-02-24 13:23:28
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
        self.handle_dict = {
            HANDLE_REFRESH: {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        self.staimg_list = {}


class STATUS_LOSS_CONNECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_BASE': {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = []

'''
Author: your name
Date: 2021-03-04 22:01:15
LastEditTime: 2021-03-07 03:27:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\status\home\work.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_WORK_SEL(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
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
            'STATUS_WORK': {
                'act_name': tool.Operation.CLICK,
                'xy': [452, 926]
            }
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/home/work/sel.png'],
            'no': []

        }

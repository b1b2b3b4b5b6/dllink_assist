'''
Author: your name
Date: 2021-03-04 21:33:52
LastEditTime: 2021-03-07 03:18:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\pvp_reg.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_ANTI_JUMP(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': {
                'act_name': tool.Operation.CLICK,
                'xy': [164, 651]
            }
        }

        recursive_update(self.transfer_dict, custom_dict)

        custom_dict = {}
        recursive_update(self.handle_dict, custom_dict)

        self.staimg_list = {
            'yes': ['img/activity/antinomy/show_up.png'],
            'no': []

        }

        self.priority = self.PRI_HIGH

'''
Author: your name
Date: 2021-02-21 23:54:10
LastEditTime: 2021-02-23 13:27:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\detect.py
'''


import tool
import logging
import except_reg
from base_reg import STATUS_BASE


class STATUS_MAIN(STATUS_BASE):

    def __init__(self):
        STATUS_BASE.__init__(self)

        self.source_list += [
        ]

        self.transfer_list += [
            {
                'target_status': STATUS_PVP,
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            {
                'target_status': STATUS_STORE,
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },
            {
                'target_status': STATUS_WORK,
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            },

            {
                'target_status': STATUS_NORMAL,
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        ]

        self.handle_list += [

        ]

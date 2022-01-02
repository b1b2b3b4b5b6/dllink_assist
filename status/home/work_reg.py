'''
Author: your name
Date: 2021-03-04 22:01:15
LastEditTime: 2022-01-03 00:45:52
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
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/home/gate/not_sel.png', True),
            'STATUS_PVP_SEL': tool.OperationClickOnImg('img/home/pvp/not_sel.png', True),
            'STATUS_STORE_SEL': tool.OperationClickOnImg('img/home/store/not_sel.png', True),
            # 'STATUS_WORK_SEL': tool.OperationClickOnImg('img/home/work/not_sel.png',True),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/home/work/sel.png'),
        ]

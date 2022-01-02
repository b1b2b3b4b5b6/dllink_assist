'''
Author: your name
Date: 2021-03-04 21:31:46
LastEditTime: 2022-01-03 00:54:18
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
            # 'STATUS_GATE_SEL': tool.OperationClickOnImg('img/home/gate/not_sel.png', True),
            'STATUS_PVP_SEL': tool.OperationClickOnImg('img/home/pvp/not_sel.png', True),
            'STATUS_STORE_SEL': tool.OperationClickOnImg('img/home/store/not_sel.png', True),
            'STATUS_WORK_SEL': tool.OperationClickOnImg('img/home/work/not_sel.png', True),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/home/gate/sel.png'),
        ]


# class STATUS_GATE_10(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_PREPARE': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [277, 834]
#             },
#             'STATUS_GATE_10': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [89, 664]
#             },
#             'STATUS_GATE_20': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [202, 664]
#             },
#             'STATUS_GATE_30': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [322, 664]
#             },
#             'STATUS_GATE_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [46, 934]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/home/gate/switch.png',
#                     'img/home/gate/level_10.png'],
#             'no': []

#         }


# class STATUS_GATE_20(STATUS_GATE_10):
#     def __init__(self):
#         super().__init__()
#         self.transfer_dict.pop('STATUS_GATE_PREPARE')
#         custom_dict = {
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': [
#                 'img/home/gate/switch.png',
#                 'img/home/gate/level_20.png'
#             ],
#             'no': []
#         }


# class STATUS_GATE_30(STATUS_GATE_10):
#     def __init__(self):
#         super().__init__()

#         self.transfer_dict.pop('STATUS_GATE_PREPARE')
#         custom_dict = {
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/home/gate/switch.png',
#                     'img/home/gate/level_30.png'],
#             'no': []

#         }


# class STATUS_GATE_PREPARE(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_DUEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [310, 834]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)


#         self.staimg_list = {
#             'yes': ['img/home/gate/prepare.png'],
#             'no': []

#         }

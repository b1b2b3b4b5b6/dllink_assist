'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-01-02 03:48:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


# class STATUS_GATE_DUEL(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [265, 913]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)
#         self.staimg_list = {
#             'yes': ['img/duel/auto_off.png'],
#             'no': []

#         }


# class STATUS_PVP_DUEL(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_PVP_PREPARE': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [60, 852]
#             }
#         }

#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/duel/key.png', 'img/duel/select.png'],
#             'no': ['img/duel/auto_off.png', 'img/duel/auto_on.png']

#         }


# class STATUS_NPC_DUEL_AUTO(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [91, 920]
#             },
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/duel/auto_on.png'],
#             'no': []
#         }

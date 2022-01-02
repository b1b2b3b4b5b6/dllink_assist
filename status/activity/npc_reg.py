'''
Author: your name
Date: 2021-03-04 21:32:39
LastEditTime: 2022-01-02 03:48:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\status\activity\npc_reg.py
'''


import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


# class STATUS_NPC_DUEL_PREPARE(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_NPC_DUEL_AUTO': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [401, 834]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/activity/npc/prepare.png'],
#             'no': []
#         }


# class STATUS_UNKNOW_DUEL_PREPARE(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_NPC_DUEL_AUTO': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [401, 834]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/activity/npc/unknow_prepare.png'],
#             'no': []

#         }

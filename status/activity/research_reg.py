'''
Author: your name
Date: 2021-03-04 21:33:52
LastEditTime: 2022-01-02 03:49:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\pvp_reg.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


# class STATUS_RECEIVE_SPECIAL_INVEST(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [302, 719]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/activity/research/recv_spec.png'],
#             'no': []

#         }


# class STATUS_RECEIVE_INVEST_COOP(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [393, 594]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/activity/research/recv.png',
#                     'img/activity/research/send_coop.png'],
#             'no': []

#         }


# class STATUS_RECEIVE_INVEST_FROM(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_GATE_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [269, 727]
#             }
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/activity/research/recv_from.png'],
#             'no': []

#         }

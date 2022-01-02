'''
Author: your name
Date: 2021-03-04 21:33:52
LastEditTime: 2022-01-03 01:52:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\pvp_reg.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_PVP_SEL(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/home/gate/not_sel.png', True),
            'STATUS_PVP': tool.OperationClickOnImg('img/home/pvp/sel.png', True),
            'STATUS_STORE_SEL': tool.OperationClickOnImg('img/home/store/not_sel.png', True),
            'STATUS_WORK_SEL': tool.OperationClickOnImg('img/home/work/not_sel.png', True),

            'STATUS_PVP_FAST': tool.OperationLeftClick([270, 512]),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/home/pvp/sel.png')
        ]


class STATUS_PVP(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/back.png', is_cache=True),
            'STATUS_PVP_PREPARE': tool.OperationClickOnImg('img/home/pvp/prepare.png', is_cache=True),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/home/pvp/prepare.png'),
            tool.ProofImg('img/home/pvp/normal_duel.png', typ='not_exist')
        ]


class STATUS_PVP_PREPARE(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_PVP': tool.OperationClickOnImg('img/base/back.png', is_cache=True),
            'STATUS_PVP_ING': tool.OperationClickOnImg('img/home/pvp/normal_duel.png', is_cache=True),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/home/pvp/prepare.png'),
            tool.ProofImg('img/home/pvp/normal_duel.png'),
        ]


# class STATUS_PVP_FAST(STATUS_BASE):

#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_PVP_ING': [tool.OperationClickOnImg('img/home/pvp/fast_duel.png', delay=10), tool.OperationRightClick(580, -14, delay=25), tool.OperationLeftClick(580, -14, delay=5)],
#         }
#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/home/pvp/fast_duel.png'],
#             'no': []
#         }


class STATUS_PVP_ING(STATUS_BASE):

    def __init__(self):
        super().__init__()

        # 空跳转方式 可以简化状态图
        custom_dict = {
            'STATUS_PVP_PREPARE': None,
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/home/pvp/ing.png', bg_app=False),
        ]

        self.priority = self.PRI_LOW


# class STATUS_PVP_HOME(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_PVP_PREPARE': {
#                 'act_name': tool.Operation.CLICK_ON_IMG,
#                 'img': 'img/home/pvp/click_to_prepare.png'
#             },
#             'STATUS_PVP_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [41, 928]
#             }
#         }

#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/home/pvp/home.png'],
#             'no': []

#         }


# class STATUS_PVP_HOME(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_PVP_PREPARE': {
#                 'act_name': tool.Operation.CLICK_ON_IMG,
#                 'img': 'img/home/pvp/click_to_prepare.png'
#             },
#             'STATUS_PVP_SEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [41, 928]
#             }
#         }

#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/home/pvp/home.png'],
#             'no': []

#         }


# class STATUS_PVP_PREPARE(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_PVP_DUEL': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [266, 428]
#             },
#             'STATUS_PVP_HOME': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [41, 928]
#             }
#         }

#         recursive_update(self.transfer_dict, custom_dict)

#         self.staimg_list = {
#             'yes': ['img/home/pvp/prepare.png'],
#             'no': []

#         }


# class STATUS_NICE(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_SEND_NICE': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [59, 863]
#             }
#         }

#         recursive_update(self.transfer_dict, custom_dict)

#

#         self.staimg_list = {
#             'yes': ['img/home/pvp/nice.png'],
#             'no': []

#         }


# class STATUS_SEND_NICE(STATUS_BASE):
#     def __init__(self):
#         super().__init__()

#         custom_dict = {
#             'STATUS_PVP_PREPARE': {
#                 'act_name': tool.Operation.CLICK,
#                 'xy': [377, 536]
#             }
#         }

#         recursive_update(self.transfer_dict, custom_dict)

#

#         self.staimg_list = {
#             'yes': ['img/home/pvp/send_nice.png'],
#             'no': []

#         }

#         self.priority = self.PRI_HIGH

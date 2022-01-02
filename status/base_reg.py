'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2022-01-03 04:38:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool
from dict_recursive_update import recursive_update


class STATUS_BASE:
    PRI_TOP = float('inf')
    PRI_HIGH = 10
    PRI_MID = 5
    PRI_LOW = 0
    PRI_BOTTOM = -float('inf')

    def __init__(self):
        self.priority = self.PRI_MID
        self.transfer_dict = {}
        self.staimg_list = []


class STATUS_SKIP(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/skip.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/skip.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_START_GAME(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/start_game.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/start_game.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_REPORT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/back.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/report.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_OK(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/ok.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/ok.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_CONFIRM(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/confirm.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/confirm.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_NEXT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/next_step.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/next_step.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_CLOSE(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/close.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/close.png')
        ]

        self.priority = self.PRI_HIGH


class STATUS_RETRY_CONNECT(STATUS_BASE):
    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/base/retry_connect.png')
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/base/retry_connect.png')
        ]

        self.priority = self.PRI_TOP

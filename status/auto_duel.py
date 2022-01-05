'''
Author: your name
Date: 2022-01-05 21:36:07
LastEditTime: 2022-01-05 21:45:10
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \dllink_assist\status\auto_duel.py
'''

import tool
import logging
from status.base_reg import STATUS_BASE
from dict_recursive_update import recursive_update


class STATUS_AUTO_DUEL_START(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            'STATUS_GATE_SEL': tool.OperationClickOnImg('img/auto_duel/start.png', True),
            'STATUS_AUTO_DUEL_ING': tool.OperationClickOnImg('img/base/back.png', is_cache=True),
        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/auto_duel/start.png')
        ]


class STATUS_AUTO_DUEL_ING(STATUS_BASE):

    def __init__(self):
        super().__init__()

        custom_dict = {
            # 空跳转方式 指代 游戏会自动转移状态
            'STATUS_GATE_SEL': None,

        }
        recursive_update(self.transfer_dict, custom_dict)

        self.staimg_list = [
            tool.ProofImg('img/auto_duel/ing.png')
        ]

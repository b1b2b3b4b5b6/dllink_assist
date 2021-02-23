'''
Author: your name
Date: 2021-02-23 11:08:45
LastEditTime: 2021-02-24 07:18:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\base_reg.py
'''
import tool

HANDLE_REFRESH = 'HANDLE_REFRESH'
HNADLE_RECONECT = 'HNADLE_RECONECT'


class STATUS_BASE:

    def __init__(self):
        self.transfer_dict = {}
        self.handle_dict = {
            HANDLE_REFRESH: {
                'act_name': tool.Operation.CLICK,
                'xy': [1, 1]
            }
        }
        self.staimg_dict = {}
        self.event_dict = {
            'EVENT_LOSE_CONNECT': {
                'img': '',
                'handle_list': [
                    {
                        'ope_name': HNADLE_RECONECT,
                        'act_name': tool.Operation.CLICK,
                        'xy': [1, 1]
                    }
                ]
            }
        }

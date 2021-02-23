'''
Author: your name
Date: 2021-02-21 01:25:38
LastEditTime: 2021-02-22 01:24:45
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\takepic.py
'''
import pyautogui
import cv2
import tool
import logging


class Base():
    base_point = None
    START = 'started'
    STOP = 'stoped'
    status = STOP

    def set_base_point(self):
        xy = tool.find_img(tool.capture_screenshot(), 'img/main/head.png')
        if xy == None:
            logging.error('can not find base_point')
            assert(None)
        else:
            self.base_point = tool.get_left_lower_point(xy)
            logging.info(f'base point is {self.base_point}')
        return self.base_point

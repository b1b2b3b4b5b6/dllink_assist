'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-02-24 14:50:37
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import pyautogui
import logging
import tool
import home_reg

logging.basicConfig(level=logging.DEBUG)
ope = tool.Operation()
ope.click([0, 0])
ope.slide([300, 300], [-100, 400])

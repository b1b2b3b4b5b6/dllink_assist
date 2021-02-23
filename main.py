'''
Author: your name
Date: 2021-02-21 01:11:28
LastEditTime: 2021-02-22 01:33:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\main.py
'''
import pyautogui
import logging
import tool
import base
import home_reg

logging.basicConfig(level=logging.DEBUG)
main = base.Base()

main.set_base_point()
ope_list = home_reg.exec()
for ope in ope_list:
    print(ope)
    ope.action()

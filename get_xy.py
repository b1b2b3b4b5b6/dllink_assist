'''
Author: your name
Date: 2021-02-24 15:28:57
LastEditTime: 2021-02-24 15:33:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\get_xy.py
'''
import os
import time
import tool
import pyautogui as pag

ope = tool.Operation()

try:
    while True:
        print("按下Ctrl + C 结束程序")
        # pag.position()返回鼠标的坐标
        x, y = pag.position()

        print(f'[{x- tool.base_point[0] }, {y- tool.base_point[1]}]')
        time.sleep(0.1)
        # 清除屏幕
        os.system('cls')
# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    print('已退出')

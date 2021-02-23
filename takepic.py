'''
Author: your name
Date: 2021-02-21 01:25:38
LastEditTime: 2021-02-21 01:45:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\takepic.py
'''
import pyautogui
import cv2

img = pyautogui.screenshot()  # x,y,w,h
img.save('screenshot.png')

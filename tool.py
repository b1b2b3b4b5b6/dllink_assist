'''
Author: your name
Date: 2021-02-21 02:27:24
LastEditTime: 2021-02-22 01:34:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\findpic.py
'''
import pyautogui
import pymouse
import numpy
import cv2 as cv
import logging


def find_img(background, target, similarity=0.95):

    source = cv.imread(background)
    template = cv.imread(target)
    cv.imshow('img', template)
    result = cv.matchTemplate(source, template, cv.TM_CCOEFF_NORMED)
    start_point = cv.minMaxLoc(result)[3]
    end_point = [start_point[0] + template.shape[1],
                 start_point[1] + template.shape[0]]

    if cv.minMaxLoc(result)[1] < similarity:
        return None
    else:
        return [start_point, end_point]


def get_center_point(xy):
    center = [sum(t) // 2 for t in zip(xy[0], xy[1])]
    return center


def get_left_lower_point(xy):
    left_lower = [xy[0][0], xy[1][1]]
    return left_lower


def get_right_upper_point(xy):
    right_upper = [xy[0][1], xy[1][0]]
    return right_upper


def capture_screenshot():
    img = pyautogui.screenshot()  # x,y,w,h
    img.save('screenshot.png')
    return 'screenshot.png'


def get_screenshot():
    return 'screenshot.png'


def click(xy):
    pymouse.PyMouse().click(xy[0], xy[1], 1)


def slide(xy_start, xy_stop):
    pymouse.PyMouse().press(xy_start[0], xy_start[1])
    pyautogui.moveTo(xy_stop[0], xy_stop[1], 0)
    pymouse.PyMouse().release(xy_stop[0], xy_stop[1])


class Operation:
    CLICK = 'click'
    SLIDE = 'slide'

    ope_name = ''
    act_name = ''
    cv_res = [None, None]

    def __str__(self):
        return f'Operation[{self.ope_name}][{self.act_name}][{self.cv_res[0]}][{self.cv_res[1]}]'

    def check_point(self, point):
        if point == None:
            logging.error(
                f'Operation[{self.ope_name}][{self.act_name}][{self.cv_res[0]}][{self.cv_res[1]}] illgal')
            assert(None)

    def action(self):
        if self.act_name == self.CLICK:
            self.check_point(self.cv_res[0])
            click(get_center_point(self.cv_res))

        elif self.act_name == self.SLIDE:
            self.check_point(self.start_point)
            if self.cv_res[0] == None and self.cv_res[1] == None:
                self.check_point(None)

            slide(self.cv_res[0], self.cv_res[1])
        else:
            self.check_point(None)

'''
Author: your name
Date: 2021-02-21 02:27:24
LastEditTime: 2022-01-03 02:17:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \挂机\findpic.py
'''

import pyautogui
import pymouse
import pykeyboard
import cv2 as cv
import logging
import time
import subprocess
import os
import threading
import pathlib
import requests


class ImgHandle():
    def __init__(self) -> None:
        pass

    @staticmethod
    def find_img(background, template_object, similarity=0.95):
        # 用于读取原生图片,现省略
        # if isinstance(template, str):
        #     template = cv.imread(template)
        result = cv.matchTemplate(
            background, template_object, cv.TM_CCOEFF_NORMED)
        start_point = cv.minMaxLoc(result)[3]
        end_point = [start_point[0] + template_object.shape[1],
                     start_point[1] + template_object.shape[0]]

        if cv.minMaxLoc(result)[1] < similarity:
            return None
        else:
            return [start_point, end_point]

    @staticmethod
    def get_center_point(xy):
        center = [sum(t) // 2 for t in zip(xy[0], xy[1])]
        return center

    @staticmethod
    def get_left_lower_point(xy):
        left_lower = [xy[0][0], xy[1][1]]
        return left_lower

    @staticmethod
    def get_right_upper_point(xy):
        right_upper = [xy[0][1], xy[1][0]]
        return right_upper


class EnvInfo():
    allow_platform = ['pc', 'android']

    platform = None
    resurce_root = None
    app_img_offset = None
    app_img_xy = None
    ft_url_prefix = None

    def __init__(self, platform):
        config_str = open('config.json', 'r', encoding='utf-8').read()
        import json
        conf = json.loads(config_str)

        self.platform = conf['platform']
        self.resurce_root = self.platform + '/'
        self.app_img_offset = conf['app_img_offset']
        self.app_img_xy = conf['app_img_xy']
        self.ft_url_prefix = conf['ft_url_prefix']

        if platform not in self.allow_platform:
            logging.error(f'platform[{platform} is not illegal]')
            assert(-1)

        logging.info(f'{self}')

    def __str__(self) -> str:
        return f'platform[{self.platform}] resurce_root[{self.resurce_root}] app_img_offset[{self.app_img_offset} app_img_xy[{self.app_img_xy} ft_url[{self.ft_url_prefix}]]'.strip()

    def get_path_by_key(self, key):
        return pathlib.PurePosixPath(
            pathlib.Path(os.path.join(self.resurce_root, key))).__str__()


class Resource():
    env_info: EnvInfo = None
    resource_obj = None
    screenshot = None
    screenshot_lock = threading.Lock()
    base_point = None

    def __init__(self, env_info: EnvInfo) -> None:
        self.env_info = env_info
        self.resource_obj = {}
        self.reset_base_point()
        # for root, dirs, files in os.walk(self.env_info.resurce_root):
        #     for file in files:
        #         file_path = pathlib.PurePosixPath(
        #             pathlib.Path(os.path.join(root, file))).__str__()
        #         key = file_path[len(self.env_info.resurce_root):]
        #         self.resource_obj[key] = cv.imread(file_path)
        #         logging.debug(
        #             f'read img obj[{key}] complete')

    def register_resource(self, key: str, object):
        if key in self.resource_obj:
            self.resource_obj[key] = object
        else:
            self.resource_obj[key] = object

        logging.debug(f'resource[{key}] register')

    def get_resource_obj(self, key: str):
        if key not in self.resource_obj:
            logging.error(f'key[{key}] not in resource_obj')
            assert(-1)
        return self.resource_obj[key]

    def refresh_screenshot(self):
        self.screenshot_lock.acquire()
        img = pyautogui.screenshot()  # x,y,w,h
        img.save('screenshot.png')
        self.screenshot = cv.imread('screenshot.png')
        self.screenshot_lock.release()

    def get_screenshot(self, refresh=False):
        if refresh == True:
            self.refresh_screenshot()

        return self.screenshot

    def get_appshot(self, refresh=False):
        if refresh == True:
            self.refresh_screenshot()

        return self.screenshot[self.get_base_point()[1]:(self.get_base_point()[1] + self.env_info.app_img_xy[1]),
                               self.get_base_point()[0]:(self.get_base_point()[0] + self.env_info.app_img_xy[0])]

    def reset_base_point(self):
        xy = ImgHandle.find_img(
            self.get_screenshot(True),
            cv.imread(self.env_info.get_path_by_key('img/base/base_point.png'))
        )
        if xy == None:
            logging.error('can not find base_point')
            assert(None)
        else:
            self.base_point = [ImgHandle.get_left_lower_point(xy)[0] + self.env_info.app_img_offset[0],
                               ImgHandle.get_left_lower_point(xy)[1] + self.env_info.app_img_offset[1]]
            logging.info(f'base point is {self.base_point}')

    def get_base_point(self):
        # if self.base_point == None:
        #     self.reset_base_point()
        return self.base_point

    def get_window_base_point(self):
        # if self.base_point == None:
        #     self.reset_base_point()
        return [self.base_point[0] - self.env_info.app_img_offset[0], self.base_point[1] - self.env_info.app_img_offset[1]]


g_resource: Resource = None
# 资源初始化


def init():
    global g_resource
    g_resource = Resource(EnvInfo('pc'))


class OperationBase:
    ope_name = None
    delay = 0

    def __init__(self, ope_name, delay=0) -> None:
        self.ope_name = ope_name
        self.delay = delay

    def action(self):
        time.sleep(self.delay)

    def __str__(self):
        return f'ope_name[{self.ope_name}] delay[{self.delay}]'.strip()


class OperationRightClick(OperationBase):
    xy = None

    def __init__(self, xy, delay=0.8) -> None:
        super().__init__('right_click', delay)
        self.xy = xy

    def __str__(self):
        return f'{super().__str__()} | xy[{self.xy}]'.strip()

    def action(self):
        pymouse.PyMouse().click(*map(sum, zip(self.xy, g_resource.get_base_point())), 2)

        super().action()


class OperationLeftClick(OperationBase):
    xy = None

    def __init__(self, xy, delay=0.8) -> None:
        super().__init__('click', delay)
        self.xy = xy

    def __str__(self):
        return f'{super().__str__()} | xy[{self.xy}]'.strip()

    def action(self):
        pymouse.PyMouse().click(*map(sum, zip(self.xy, g_resource.get_base_point())), 1)

        super().action()


class OperationClickOnImg(OperationBase):
    img_key = None
    is_cache = None
    last_xy = None

    def __init__(self, img_key, is_cache=False, delay=0.8) -> None:
        super().__init__('click_on_img', delay)
        self.img_key = img_key
        self.is_cache = is_cache
        g_resource.register_resource(img_key, cv.imread(
            g_resource.env_info.get_path_by_key(img_key)))

    def __str__(self):
        return f'{super().__str__()} | img[{self.img_key}] is_cache[{self.is_cache}]'.strip()

    def action(self):
        if self.is_cache == True and self.last_xy != None:
            pass
        else:
            res = ImgHandle.find_img(
                g_resource.get_appshot(), g_resource.get_resource_obj(self.img_key))
            if res == None:
                logging.error(
                    f'can not action click on img_key[{self.img_key}]')
            else:
                self.last_xy = ImgHandle.get_center_point(res)

        pymouse.PyMouse().click(*map(sum, zip(self.last_xy, g_resource.get_base_point())), 1)

        super().action()


class OperationSlide(OperationBase):
    xy_start = None
    xy_stop = None

    def __init__(self, xy_start, xy_stop, delay=0) -> None:
        super().__init__('slide', delay)
        self.xy_start = xy_start
        self.xy_stop = xy_stop

    def __str__(self):
        return f'{super().__str__()} | xy_start[{self.xy_start}] xy_stop[{self.xy_stop}]'.strip()

    def action(self):
        pymouse.PyMouse().press(*map(sum, zip(self.xy_start, g_resource.get_base_point())))
        pyautogui.moveTo(
            *map(sum, zip(self.xy_stop,  g_resource.get_base_point())), 0.3)
        pymouse.PyMouse().release(*map(sum, zip(self.xy_stop,  g_resource.get_base_point())))
        super().action()


class Proof():
    def __init__(self) -> None:
        pass

    def get_result() -> bool:
        return True

    def __str__(self) -> str:
        return ''


class ProofImg(Proof):
    allow_typ = ['exist', 'not_exist']
    img_key = None
    typ = None
    bg_app = None

    def __init__(self, img_key, typ='exist', bg_app=True) -> None:
        super().__init__()
        self.img_key = img_key
        self.typ = typ
        self.bg_app = bg_app
        if typ not in self.allow_typ:
            logging.error(f'illegal proofimg: {self}')
            assert(-1)

        g_resource.register_resource(img_key, cv.imread(
            g_resource.env_info.get_path_by_key(img_key)))

    def __str__(self) -> str:
        return f'{super().__str__()} | ProofImg: img_key[{self.img_key}] typ[{self.typ}]'.strip()

    def get_result(self) -> bool:
        if self.bg_app == True:
            bg = g_resource.get_appshot()
        else:
            bg = g_resource.get_screenshot()

        if self.typ == 'exist':
            xy = ImgHandle.find_img(
                bg, g_resource.get_resource_obj(self.img_key))

            if xy == None:
                logging.debug(
                    f'{self} | can not proof]')
                return False

        elif self.typ == 'not_exist':
            xy = ImgHandle.find_img(
                bg, g_resource.get_resource_obj(self.img_key))

            if xy != None:
                logging.debug(
                    f'{self} | can not proof]')
                return False

        return True


def retry(func, count=1, delay=0):
    if count == 0:
        logging.error(f'retry count can not[{count}] < 0')
        assert(None)

    for n in range(count):
        if func() == True:
            return True
        time.sleep(delay)
    return False


def log_error_screen(name):
    img = pyautogui.screenshot()  # x,y,w,h
    img.save(time.strftime('err_%m%d%H%M%S_',
                           time.localtime()) + name + '.png')


def kick_ass():
    k = pykeyboard.PyKeyboard()
    k.tap_key(k.control_key)


# 点击一个无关紧要的地方
def kick_all():
    logging.info('need final solution')
    log_error_screen('kick_all')
    xy = g_resource.env_info.app_img_xy
    for x in range(1, xy[0]-1, xy[0] // 9):
        for y in range(1, xy[1]-1, xy[1] // 16):
            OperationLeftClick([x, y], delay=0.01).action()
    logging.info('final solution complete')


def push_cloud(msg):
    requests.get(
        f'{msg}')


def get_all_modules(dir_name):
    modules = []
    for root, _, fs in os.walk(dir_name):
        for f in fs:
            if f.startswith('__') or f.endswith('.pyc'):
                continue
            fullname = os.path.join(root, f)
            fullname = fullname.replace('.py', '')
            fullname = fullname.replace('\\', '.')
            modules.append(fullname)
    return modules


# 视平台而定,以下仅适用于雷电模拟器
# class SwitchApp():
#     def game(self):
#         logging.info('switch to game')
#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/game_ico.png', bg_app=False).action('screen')

#     def home(self):
#         logging.info('switch to home')
#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/head.png', bg_app=False).action('screen')


# class GameControl():
#     def stop(self):
#         logging.info('close game')

#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/home.png').action('screen')
#         time.sleep(1)

#         kb = pykeyboard.PyKeyboard()
#         kb.tap_key(kb.function_keys[1])
#         time.sleep(0.5)

#         kb = pykeyboard.PyKeyboard()
#         kb.tap_key(kb.function_keys[2])
#         time.sleep(0.5)

#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/clear.png').action('app')
#         time.sleep(1)

#     def start(self):
#         logging.info('start game')
#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/home.png').action('screen')
#         time.sleep(1)

#         kb = pykeyboard.PyKeyboard()
#         kb.tap_key(kb.function_keys[1])
#         time.sleep(0.5)

#         g_resource.refresh_screenshot()
#         Operation(Operation.CLICK_ON_IMG,
#                   img='img/base/desk_icon.png').action('app')
#         time.sleep(5)

#     def restart(self):
#         logging.info('restart game')
#         self.stop()
#         self.start()


# 暂无断网功能
class Internet():
    def open(self):
        logging.info('internet open')
        subprocess.call('NetDisabler_x64.exe /E')

    def close(self):
        logging.info('internet close')
        subprocess.call('NetDisabler_x64.exe /D')

    def reboot(self, time_s):
        logging.info(f'internet will reboot[{time_s}]')
        self.close()
        time.sleep(time_s)
        self.open()

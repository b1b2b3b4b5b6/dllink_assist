'''
Author: your name
Date: 2021-02-24 06:17:11
LastEditTime: 2021-03-07 03:48:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\transfer.py
'''


import inspect
import tool
import sys
import networkx as nx
import matplotlib.pyplot as plt
import logging
import threading
import time
from dict_recursive_update import recursive_update
import collections
import cv2 as cv
import importlib
import duel
from pathlib import Path

delay_dict = {
    'STATUS_GATE_DUEL': 16000,
    'STATUS_PVP_DUEL': 20000,
    "STATUS_NPC_DUEL_AUTO": 10000,
    'STATUS_PVP_HOME': 2000,
    'STATUS_PVP_PREPARE': 2000,
    'STATUS_SEND_NICE': 1000
}

duel_list = ['STATUS_PVP_DUEL', 'STATUS_GATE_DUEL']


class StatusControlThread(threading.Thread):

    now_status = 'STATUS_BASE'
    target_status = 'STATUS_BASE'
    next_status = 'STATUS_BASE'
    status_dict = d1 = collections.OrderedDict()
    G = nx.DiGraph()
    short_path_dict = {}
    thread_close_flag = False
    img_dict = {}

    def __init__(self):
        super().__init__()
        tool.Operation()

        for mn in tool.get_all_modules('status'):
            importlib.import_module(mn)
            for name, class_ in inspect.getmembers(sys.modules[mn], inspect.isclass):
                self.status_dict[name] = class_()
                for k, _ in self.status_dict[name].transfer_dict.items():
                    self.G.add_edge(name, k)
                for img in (self.status_dict[name].staimg_list['yes'] + self.status_dict[name].staimg_list['no']):
                    if False == Path(img).exists():
                        logging.error(f'[{img}] not exist')
                        assert(None)
                    self.img_dict[img] = cv.imread(img)

        self.status_dict.pop('STATUS_BASE')
        z = list(zip(self.status_dict.keys(), self.status_dict.values()))
        z = sorted(z, key=lambda x: x[1].priority, reverse=True)
        self.status_dict = dict(z)

        self.short_path_dict = dict(nx.all_pairs_shortest_path(self.G))
        self.search_status()

    def __str__(self):
        return f'now[{self.now_status}] next[{self.next_status}] target[{self.target_status}]'

    def goto_status(self, status, delay_s=180):
        logging.info(f'start go to status[{status}] ')
        if self.now_status == status:
            return True
        self.set_target_status(status)
        if delay_s == 0:
            while self.now_status != status:
                time.sleep(1)
        else:
            while delay_s >= 0 and self.now_status != status:
                time.sleep(1)
                delay_s -= 1
        if self.now_status == status:
            logging.info(f'start go to status[{status}] success')
            return True
        else:
            logging.warn(f'start go to status[{status}] fail')
            return False

    def exec_delay(self, status):
        if status in delay_dict.keys():
            logging.info(f'exec [{status}] delay[{delay_dict[status]}]')
            time.sleep(delay_dict[status] / 1000)
        else:
            time.sleep(1000 / 1000)

    def transfer(self, status, delay_ms=500):
        next_status_dict = self.status_dict[self.now_status].transfer_dict

        default_dict = {'xy': [0, 0], 'img': ''}
        recursive_update(default_dict, next_status_dict[status])
        ope = tool.Operation(default_dict['act_name'], [
            default_dict['xy']], default_dict['img'])
        ope.action()

        self.exec_delay(status)

    def run(self):  # 必须有的函数
        self.thread_close_flag = False
        while True:
            if self.thread_close_flag:
                exit()
            if self.target_status == 'STATUS_BASE':
                time.sleep(0.5)
                continue

            self.search_status(refresh=True)

            if self.now_status == 'STATUS_BASE':
                continue

            if self.now_status in duel_list:
                duel.run_loop(self.now_status)
                self.now_status = 'STATUS_BASE'
                continue

            if self.now_status != self.target_status:
                if self.target_status not in self.short_path_dict[self.now_status]:
                    logging.error(f'can not reach targer status, {self}')
                    assert(None)
                self.next_status = self.short_path_dict[self.now_status][self.target_status][1]
                logging.info(f'start transfer, {self}')
                self.transfer(self.next_status)
                continue

    def stop(self):
        self.thread_close_flag = True
        self.join()

    def show_map(self):
        for k, v in self.short_path_dict.items():
            print(k)
            print(v)
        nx.draw(self.G, with_labels=True, edge_color='b',
                node_color='g', node_size=1000)
        plt.show()

    def check_status(self, expect_status, refresh=True):
        if refresh == True:
            tool.capture_screenshot()
        cs = self.status_dict[expect_status]

        res = True
        for img in cs.staimg_list['yes']:
            xy = tool.find_img(tool.get_appshot(), self.img_dict[img])
            if xy == None:
                logging.debug(
                    f'expect status[{expect_status}] can not find img[{img}]')
                res = False
                break

        for img in cs.staimg_list['no']:
            xy = tool.find_img(tool.get_appshot(), self.img_dict[img])

            if xy != None:
                logging.debug(
                    f'expect status[{expect_status}] find illgal img[{img}]')
                res = False
                break

        return res

    def search_status(self, refresh=True):

        def check():
            if refresh == True:
                tool.capture_screenshot()
            self.now_status = 'STATUS_BASE'

            for s in self.status_dict.keys():
                if self.check_status(s, False) == True:
                    self.now_status = s
                    return True
            tool.kick_ass()
            return False

        if tool.retry(check, 60, 1000) == False:
            logging.error('can not search status')
            tool.log_error_screen('search_status')
            assert(None)
            return False
        logging.info(f'search status finished, {self}')
        return True

    def set_target_status(self, expect_status):
        self.target_status = expect_status

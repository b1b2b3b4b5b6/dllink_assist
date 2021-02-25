'''
Author: your name
Date: 2021-02-24 06:17:11
LastEditTime: 2021-02-25 21:50:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\transfer.py
'''


import base_reg
import inspect
import tool
import sys
import home_reg
import duel
import base_reg
import networkx as nx
import matplotlib.pyplot as plt
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG)

reg_list = ['base_reg', 'home_reg']

delay_dict = {
    'STATUS_TRANSDOOR_DUEL': 14000
}


class StatusControlThread(threading.Thread):

    now_status = 'STATUS_BASE'
    target_status = 'STATUS_BASE'
    next_status = 'STATUS_BASE'
    status_dict = {}
    G = nx.DiGraph()
    short_path_dict = {}
    thread_close_flag = False

    def exec_delay(self, status):
        if status in delay_dict.keys():
            logging.info(f'exec [{status}] delay[{delay_dict[status]}]')
            time.sleep(delay_dict[status] / 1000)
        else:
            time.sleep(1000 / 1000)

    def transfer(self, status, delay_ms=500):
        next_status_dict = self.status_dict[self.now_status].transfer_dict
        if status not in next_status_dict:
            logging.error(
                f'{[self.now_status]} not have next status[{status}]')
            tool.log_error_screen('transfer_illgal')
            assert(None)
        ope = tool.Operation(tool.Operation.CLICK, [
                             next_status_dict[status]['xy']])
        ope.action()

        self.exec_delay(status)
        if self.check_status(status) == True:
            self.now_status = status
            logging.info(f'transfer success, {self}')
        else:
            self.now_status = 'STATUS_BASE'
            logging.info(f'transfer fail, {self}')

    def run(self):  # 必须有的函数
        self.thread_close_flag = False
        while True:
            if self.thread_close_flag:
                exit()
            if self.target_status == 'STATUS_BASE':
                time.sleep(0.2)
                continue

            if self.now_status == 'STATUS_BASE':
                self.search_status()
                continue

            if self.now_status == 'STATUS_TRANSDOOR_DUEL':
                duel.loop()
                self.now_status = 'STATUS_BASE'
                continue

            if self.now_status != self.target_status:
                if self.target_status not in self.short_path_dict[self.now_status]:
                    logging.error(f'can not reach targer status, {self}')
                    assert(None)
                self.next_status = self.short_path_dict[self.now_status][self.target_status][1]

                self.transfer(self.next_status)

    def stop(self):
        self.thread_close_flag = True
        self.join()

    def __init__(self):
        super().__init__()
        for mn in reg_list:
            for name, class_ in inspect.getmembers(sys.modules[mn], inspect.isclass):
                self.status_dict[name] = class_()
                for k, _ in self.status_dict[name].transfer_dict.items():
                    self.G.add_edge(name, k)
        self.status_dict.pop('STATUS_BASE')
        self.short_path_dict = dict(nx.all_pairs_shortest_path(self.G))
        self.search_status()

    def __str__(self):
        return f'now_status[{self.now_status}] next_status[{self.next_status}] target_status[{self.target_status}]'

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
        staimg_list = cs.staimg_list
        res = True
        for img in staimg_list:
            xy = tool.find_img(tool.get_screenshot(), img)

            if xy == None:
                logging.debug(
                    f'expect status[{expect_status}] can not find img[{img}]')
                res = False
                break
        return res

    def search_status(self, refresh=True):

        def check():
            if refresh == True:
                tool.capture_screenshot()
            self.now_status = 'STATUS_BASE'
            for s in self.status_dict:
                if self.check_status(s, False) == True:
                    self.now_status = s
                    return True
            return False

        if tool.retry(check, 3, 500) == False:
            logging.error('can not search status')
            tool.log_error_screen('search_status')
            assert(None)
            return False
        logging.info(f'search status finished, {self}')
        return True

    def set_target_status(self, expect_status):
        self.target_status = expect_status

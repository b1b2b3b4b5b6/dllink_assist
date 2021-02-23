'''
Author: your name
Date: 2021-02-24 06:17:11
LastEditTime: 2021-02-24 07:20:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \dllink_assist\transfer.py
'''

import networkx as nx
import matplotlib.pyplot as plt
import base_reg
import inspect
import sys
import home_reg
import base_reg
import networkx as nx
import matplotlib.pyplot as plt


reg_list = ['base_reg', 'home_reg']
status_dict = {}

G = nx.DiGraph()
for mn in reg_list:
    for name, class_ in inspect.getmembers(sys.modules[mn], inspect.isclass):
        status_dict[name] = class_()
        for k, v in status_dict[name].transfer_dict.items():
            G.add_edge(name, k)


nx.draw(G, with_labels=True, edge_color='b', node_color='g', node_size=1000)
plt.show()

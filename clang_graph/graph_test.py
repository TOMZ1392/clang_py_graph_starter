# -*- coding: utf-8 -*-
"""
Created on Wed May 24 23:17:50 2023

@author: T
"""

import networkx as nx

G=nx.Graph()
rel_list=[{'ProcessDataA':['getItemB','getItemC']},{'processB':['processE','processF']},{'processK':['ProcessDataA','processR']}]

for i in rel_list:
    k=[*i][0]
    G.add_node(k)
    for j in i[k]:
        G.add_node(j)
        G.add_edge(k,j)
#G.add_nodes_from(rel_list)

nx.draw(G, with_labels=1)

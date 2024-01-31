import networkx as nx

G=nx.Graph()
#rel_list=[{'A':['B','C']},{'B':['E','F']},{'K':['A','R']}]
#G.add_nodes_from(rel_list)
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])
nx.draw(G)

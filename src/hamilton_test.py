"""
This module implements some proves to check efficiency of hamilton method. 
We compare it with a simple backtrack search provided by mikkelam
"""


import random
import time
from graph import Graph
import networkx as nx

def hamilton(G):
    """
    Código obtenido de https://gist.github.com/mikkelam/ab7966e7ab1c441f947b.
    Todo el crédito de esta función es de   mikkelam
    """

    F = [(G,[list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        for node in graph.neighbors(path[-1]):
            conf_p = path[:]
            conf_p.append(node)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return None

def experiment(graph):
    print('Graph info:')
    print(' - vertices:', len(graph.vertices()))
    print(' - edges:', len(graph.edges()))
    print()

    start_time = time.time()
    print('SAT solving - ')
    path = graph.find_hamiltonian_path()
    print('Solving last: ', (time.time() - start_time), 'segs.')
    #    print('Checking correctness:', check_correctness(graph, path))
    print(path)
    print('\n\n')

    print('Backtrack solving - ')
    start_time = time.time()
    path =     internet_hamilton(list(graph.edges()))
    print('Solving last: ', (time.time() - start_time), 'segs.')
    # print('Checking correctness:', hamilton.check_correctness(graph, path))
    print('\n\n')


if __name__ == '__main__':
    graph_list = [
        'graphs/structured-type1-100nodes.txt',
        'graphs/structured-type1-400nodes.txt',
    ]

    for filename in graph_list:
        graph = Graph()
        graph.add_from_text(filename)
        experiment(graph)


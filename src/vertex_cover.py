import time
import math
import random

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF, CNFPlus




def minimun_cover(graph):
    old = len(graph)
    new = len(graph) // 2

    while old != new:
        if vertex_cover(graph, new, False):
            old = new
            new = new // 2

        else:
            new += math.ceil((old - new) / 2)

    return new


def random_graph(n_vertices, n_edges):
    graph = Graph()
    for i in range(n_vertices):
        graph.add_vertex(str(i))

    for i in range(n_edges):
        ori = random.randint(0, n_vertices - 1)
        des = random.randint(0, n_vertices - 1)
        graph.add_edge(str(ori), str(des))

    return graph


rg = random_graph(19, 5)
graph = Graph(rg)
print(rg)
print(minimun_cover(graph))

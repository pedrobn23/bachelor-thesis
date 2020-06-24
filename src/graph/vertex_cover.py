import time
import math
import random

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF, CNFPlus


def vertex_cover(graph, k=1, verbose=True):
    """
    Check if there exists a vertex cover of, at most, k-vertices.
    """
    if not graph.edges():
        return []

    if verbose:
        print('\nCodifying SAT Solver...')

    length = len(graph.vertices())
    solver = Solver(name='cd')
    names = {}

    vpool = IDPool()
    vertices_ids = [vpool.id(vertex) for vertex in graph.vertices()]

    if verbose:
        print(' -> Codifying: Every vertex must be accessible')

    for vertex in graph.vertices():
        solver.add_clause(
            [vpool.id(vertex)] +
            [vpool.id(adjacent_vertex) for adjacent_vertex in graph[vertex]])

    if verbose:
        print(' -> Codifying: At most', k, 'vertices should be selected')

    cnf = CardEnc.atmost(lits=vertices_ids, bound=k, vpool=vpool)

    solver.append_formula(cnf)

    if verbose:
        print('Running SAT Solver...')
    return solver.solve()


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

rg = random_graph(19,5)
graph = Graph(rg)
print(rg)
print(minimun_cover(graph))

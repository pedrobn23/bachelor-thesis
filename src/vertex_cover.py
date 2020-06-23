import time
import math

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
        print(' -> Codifying: At most', k ,'vertices should be selected')

    cnf = CardEnc.atmost(lits=vertices_ids,
                         bound=k,
                         vpool=vpool)

    solver.append_formula(cnf)

    if verbose:
        print('Running SAT Solver...')
    return solver.solve()


def minimun_cover(graph):
    old = len(graph)
    new = len(graph)//2

    while old != new:
        if vertex_cover(graph, new, False):
            old = new
            new = new // 2

        else:
            new += math.ceil((old - new) / 2)

    return new

g2 = {"a": {"b", "c"}, "b": {"a"}, "c": {"a"}}
graph = Graph(g2)
print(vertex_cover(graph,2))


import time
import math
import random

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF


def coloring(graph, n_color=4, verbose=True):
    """
    Check if there exists a vertex coloring of, at most, k-vertices.
    """
    if n_color < 0:
        raise ValueError('Number of colors must be positive integer')

    if n_color == 0:
        return not bool(graph.vertices())

    if verbose:
        print('\nCodifying SAT Solver...')

    length = len(graph.vertices())
    solver = Solver(name='cd')
    names = {}
    cnf = CNF()

    vpool = IDPool()

    if verbose:
        print(' -> Codifying: Every vertex must have a color, and only one')

    for vertex in graph.vertices():
        cnf = CardEnc.equals(lits=[
            vpool.id('{}color{}'.format(vertex, color))
            for color in range(n_color)
        ],
                             vpool=vpool,
                             encoding=0)

        solver.append_formula(cnf)

    if verbose:
        print(' -> Codifying: No two neighbours can have the same color')

    visited = set()
    for vertex in graph.vertices():
        for neighbour in graph[vertex]:
            for color in range(n_color):
                solver.add_clause([
                    -vpool.id('{}color{}'.format(vertex, color)),
                    -vpool.id('{}color{}'.format(neighbour, color))
                ])
    if verbose:
        print('Running SAT Solver...')
    return solver.solve()


def minimun_coloring(graph):
    old = len(graph)
    new = len(graph) // 2

    while old != new:
        if coloring(graph, new, False):
            old = new
            new = new // 2
        else:
            new += math.ceil((old - new) / 2)

    return new

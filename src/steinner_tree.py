import time
import math
import random

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF


def steinner_tree(graph, distance=4, verbose=True):
    """
    Check if there exists a vertex cover of, at most, k-vertices.
    """
    if n_color < 0:
        raise ValueError('Number of colors must be positive integer')

    if n_color == 0:
        return not bool(graph.vertices())

    if verbose:
        print('\nCodifying SAT Solver...')

    length = len(graph.vertices())
    solver = Solver(name='cd')
    vertices = graph.vertices()
    cnf = CNF()

    vpool = IDPool()

    if verbose:
        print(' -> Codifying: at most k edges should be selected')
        
    if verbose:
        print('Running SAT Solver...')
    return solver.solve()

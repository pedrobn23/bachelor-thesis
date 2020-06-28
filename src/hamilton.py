"""
Module implements two versions of the
problem of finding a Hamiltonian path.

Implements a function find_hamiltonian_path
that reduces the problem to SAT.

We uses internally the CaDiCaL solver.
"""

from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from graph import Graph
from utility import xvar
    


def check_correctness(graph, path):
    """
    Check the correctness of a path in
    order to solve the Hamiltonian path
    """
    if path:
        length = len(graph)
        for i in range(length - 1):
            if path[(i + 1)] not in graph[path[i]]:
                return False
    return True


print(xvar(1,2))

graph2 = {"a": {"b"}, "b": {"c","a"}, "c": {"b"}}

graph = Graph(graph2)
path = find_hamiltonian_path(graph, check_cycle=True)
print(check_correctness(graph, path), path)

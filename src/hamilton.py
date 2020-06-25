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
    


def find_hamiltonian_path(graph, check_cycle=False):
    """
    should it exists, find a Hamiltonian on
    current graph. Otherwise return empty list.
    """
    if not graph.edges():
        return []

    print('Codifying SAT Solver...')
    length = len(graph.vertices())
    solver = Solver(name='cd')
    names = {}
    vpool = IDPool()

    for integer, vertex in enumerate(graph.vertices()):
        names[integer + 1] = vertex
    names[0] = names[length]
        

    
    for position_in_path in range(length):
        for vertex in range(1, length + 1):
            vpool.id('v{}pos{}'.format(vertex, position_in_path))
               
    print(' -> Codifying: All Positions occupied')
    for position_in_path in range(length):
        var_list = [
            vpool.id('v{}pos{}'.format(vertex, position_in_path))
            for vertex in range(1, length + 1)
        ]

        cnf = CardEnc.equals(lits=var_list, encoding=0, vpool=vpool)
        print(cnf.clauses)
        solver.append_formula(cnf)

    print(' -> Codifying: All vertex visited')
    for vertex in range(1, length + 1):
        var_list = [
            vpool.id('v{}pos{}'.format(vertex, position_in_path))
            for position_in_path in range(length)
        ]

        cnf = CardEnc.equals(lits=var_list, encoding=EncType.pairwise, vpool=vpool)
        print(cnf.clauses)
        solver.append_formula(cnf)

    print(' -> Codifying: Adjacency Matrix')
    edges = graph.edges()
    for vertex_a in range(1, length + 1):
        for vertex_b in range(vertex_a + 1, length + 1):
            if (names[vertex_a], names[vertex_b]) not in edges:
                for position_in_path in range(length - 1):
                    solver.add_clause([
                        -vpool.id(vertex_a, position_in_path),
                        -((position_in_path + 1) * length + vertex_b)
                    ])
                    solver.add_clause([
                        -(position_in_path * length + vertex_b),
                        -((position_in_path + 1) * length + vertex_a)
                    ])

                if check_cycle:
                    solver.add_clause(
                        [-vertex_b, -(length * (length - 1) + vertex_a)])
                    solver.add_clause(
                        [-vertex_a, -(length * (length - 1) + vertex_b)])

    print('Running SAT Solver...')
    solution = []
    if solver.solve():
        for variable in solver.get_model():
            if variable > 0:
                solution.append(names[variable % length])

    return solution


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

graph2 = {"a": {"b", "c"}, "b": {"c"}, "c": {"b"}}

graph = Graph(graph2)
path = find_hamiltonian_path(graph, check_cycle=True)
print(check_correctness(graph, path), path)

from graph import Graph
from pysat.solvers import Solver


def find_hamiltonian_path(graph):
    """
    should it exists, find a Hamiltonian on
    current graph. Otherwise return empty list.
    """

    if not graph.edges():
        return []

    length = len(graph.vertices())
    solver = Solver(name='cd')
    names = {}

    for integer, vertex in enumerate(graph.vertices()):
        names[integer + 1] = vertex
    names[0] = names[length]

    # Every position in the path must be occupied
    for position_in_path in range(1, length + 2):
        solver.add_clause([
            position_in_path * length + vertex
            for vertex in range(1, length + 1)
        ])

    # Every vertex must have a position in path
    for vertex in range(1, length + 1):
        solver.add_clause([
            position_in_path * length + vertex
            for position_in_path in range(1, length + 2)
        ])

    # Only one vertex must have a position in path
    for position_in_path in range(1, length + 2):
        for vertex_a in range(1, length + 1):
            for vertex_b in range(vertex_a + 1, length + 1):
                solver.add_clause([
                    -(position_in_path * length + vertex_a),
                    -(position_in_path * length + vertex_b)
                ])

    #every vertes must have only one position
    for position_in_path in range(1, length + 1):
        for position_in_path2 in range(position_in_path + 1, length + 1):
            for vertex_a in range(1, length + 1):
                solver.add_clause([
                    -(position_in_path * length + vertex_a),
                    -(position_in_path2 * length + vertex_a)
                ])

        if position_in_path > 1:
            for vertex_a in range(1, length + 1):
                solver.add_clause([
                    -(position_in_path * length + vertex_a),
                    -((length + 1) * length + vertex_a)
                ])

    # Every two consecutive vertex has to be adjacent
    edges = graph.edges()
    for vertex_a in range(1, length + 1):
        for vertex_b in range(vertex_a, length + 1):
            if (names[vertex_a], names[vertex_b]) not in edges:
                for position_in_path in range(1, length + 1):
                    solver.add_clause([
                        -(position_in_path * length + vertex_a),
                        -((position_in_path + 1) * length + vertex_b)
                    ])

    solution = []
    solver.solve()
    if solver.solve():
        for variable in solver.get_model():
            if variable > 0 and variable > length:
                solution.append(names[variable % length])

    return solution


def find_hamiltonian_path2(graph):
    """
    should it exists, find a Hamiltonian on
    current graph. Otherwise return empty list.
    """

    if not graph.edges():
        return []

    length = len(graph.vertices())
    solver = Solver(name='cd')
    names = {}

    for integer, vertex in enumerate(graph.vertices()):
        names[integer + 1] = vertex
    names[0] = names[length]

    cnf = CardEnc.equals(lits=[1, 2, 3], encoding=EncType.pairwise)
    # Every position in the path must be occupied
    for position_in_path in range(1, length + 2):
        solver.add_clause([
            position_in_path * length + vertex
            for vertex in range(1, length + 1)
        ])

    # Every vertex must have a position in path
    for vertex in range(1, length + 1):
        solver.add_clause([
            position_in_path * length + vertex
            for position_in_path in range(1, length + 2)
        ])

    # Only one vertex must have a position in path
    for position_in_path in range(1, length + 2):
        for vertex_a in range(1, length + 1):
            for vertex_b in range(vertex_a + 1, length + 1):
                solver.add_clause([
                    -(position_in_path * length + vertex_a),
                    -(position_in_path * length + vertex_b)
                ])

    #every vertes must have only one position
    for position_in_path in range(1, length + 1):
        for position_in_path2 in range(position_in_path + 1, length + 1):
            for vertex_a in range(1, length + 1):
                solver.add_clause([
                    -(position_in_path * length + vertex_a),
                    -(position_in_path2 * length + vertex_a)
                ])

        if position_in_path > 1:
            for vertex_a in range(1, length + 1):
                solver.add_clause([
                    -(position_in_path * length + vertex_a),
                    -((length + 1) * length + vertex_a)
                ])

    # Every two consecutive vertex has to be adjacent
    edges = graph.edges()
    for vertex_a in range(1, length + 1):
        for vertex_b in range(vertex_a, length + 1):
            if (names[vertex_a], names[vertex_b]) not in edges:
                for position_in_path in range(1, length + 1):
                    solver.add_clause([
                        -(position_in_path * length + vertex_a),
                        -((position_in_path + 1) * length + vertex_b)
                    ])

    solution = []
    solver.solve()
    if solver.solve():
        for variable in solver.get_model():
            if variable > 0 and variable > length:
                solution.append(names[variable % length])

    return solution

graph = Graph()
graph.add_from_text('graphs/structured-type1-100nodes.txt')
print(find_hamiltonian_path(graph))

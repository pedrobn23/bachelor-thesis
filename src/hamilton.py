from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType


def find_hamiltonian_path(graph):
    """
    should it exists, find a Hamiltonian on
    current graph. Otherwise return empty list.
    """
    print('Codifying SAT problem...')
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

    print('Solving SAT problem...')
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

    # Every position in the path must be occupied
    for position_in_path in range(length):
        var_list = [
            position_in_path * length + vertex
            for vertex in range(1, length + 1)
        ] 

        cnf = CardEnc.equals(lits=var_list, encoding=EncType.pairwise)
        print(cnf.clauses)
        solver.append_formula(cnf)
    print()

    # Every vertex must have a position in path
    for vertex in range(1, length + 1):
        var_list = [
            position_in_path * length + vertex
            for position_in_path in range(length)
        ]
        
        cnf = CardEnc.equals(lits=var_list, encoding=EncType.pairwise)
        solver.append_formula(cnf)
        print(cnf.clauses)

    print()
    # Every two consecutive vertex has to be adjacent
    edges = graph.edges()
    for vertex_a in range(1, length + 1):
        for vertex_b in range(vertex_a+1, length + 1):
            print(vertex_a, vertex_b)
            if (names[vertex_a], names[vertex_b]) not in edges:
                print('not consecutive')
                for position_in_path in range(length-1):
                    solver.add_clause([
                        -(position_in_path * length + vertex_a),
                        -((position_in_path + 1) * length + vertex_b)
                    ])
                    solver.add_clause([
                        -(position_in_path * length + vertex_b),
                        -((position_in_path + 1) * length + vertex_a)
                    ])

                solver.add_clause([-vertex_b,-(length*(length-1) + vertex_a)  ])
                solver.add_clause([-vertex_a,-(length*(length-1) + vertex_b)  ])



    solution = []
    if solver.solve():
        for variable in solver.get_model():
            if variable > 0:
                solution.append(names[variable % length])

    return solution




g2 = {"a": {"b","c"}, "b": {"c","a"}, "c": {"b","a"}}
graph = Graph(g2)
# graph.add_from_text('graphs/structured-type1-100nodes.txt')
print(find_hamiltonian_path2(graph))

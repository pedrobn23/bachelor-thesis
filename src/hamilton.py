from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType


def find_hamiltonian_path(graph):
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

    for integer, vertex in enumerate(graph.vertices()):
        names[integer + 1] = vertex
    names[0] = names[length]

    print(' -> Codifying: All Positions occupied')
    # Every position in the path must be occupied
    for position_in_path in range(length):
        var_list = [
            position_in_path * length + vertex
            for vertex in range(1, length + 1)
        ] 

        cnf = CardEnc.equals(lits=var_list, encoding=0)
        print(cnf.clauses)
        solver.append_formula(cnf)


    print(' -> Codifying: All vertex visited')
    # Every vertex must have a position in path
    for vertex in range(1, length + 1):
        var_list = [
            position_in_path * length + vertex
            for position_in_path in range(length)
        ]
        
        cnf = CardEnc.equals(lits=var_list, encoding=EncType.pairwise)
        solver.append_formula(cnf)

    print(' -> Codifying: Adjacency Matrix')
    # Every two consecutive vertex has to be adjacent
    edges = graph.edges()
    for vertex_a in range(1, length + 1):
        for vertex_b in range(vertex_a+1, length + 1):
            if (names[vertex_a], names[vertex_b]) not in edges:
                print(names[vertex_a], names[vertex_b])
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


        

    print('Running SAT Solver...')
    solution = []
    if solver.solve():
        for variable in solver.get_model():
            if variable > 0:
                solution.append(names[variable % length])

    return solution



g2 = {"a":{'b','c'},'b':{'a','c'}, 'c':{'a','b'}}
graph = Graph(g2)
#graph.add_from_text('graphs/structured-type1-400nodes.txt')
print(find_hamiltonian_path(graph))

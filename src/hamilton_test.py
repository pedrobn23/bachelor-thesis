import random
import time
from graph import Graph
from hamilton import find_hamiltonian_path, check_correctness

def random_graph(n_vertices, n_edges):
    graph = Graph()

    for i in range(n_vertices):
        graph.add_vertex(str(i))

    for i in range(n_edges):
        ori = randint(0, n_vertices)
        des = randint(0, n_vertices)
        graph.add_edge(ori, des)

    return graph
        

def experiment(graph):
        start_time =  time.time()
        path = find_hamiltonian_path(graph)
        print('Solving last: ',(time.time() - start_time), 'segs.')
        print('Checking correctness:', check_correctness(graph, path))


if name == '__main__':
    graph_list = [
        'graphs/structured-type1-100nodes.txt'
        ]
    
    for filename in graph_list():
        graph = Graph()
        graph.add_from_text(filename)
        experiment(graph)

    for n_vertex in range(100,250,30):
        for n_edges in range(100,1000,100):
            graph = random_graph(n_vertices, n_edges)
            experiment(graph)

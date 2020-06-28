import random
import time
import hamilton
from graph import Graph


def random_graph(n_vertices, n_edges):
    graph = Graph()
    for i in range(n_vertices):
        graph.add_vertex(str(i))

    while len(graph.edges()) < n_edges:
        ori = random.randint(0, n_vertices - 1)
        des = random.randint(0, n_vertices - 1)
        graph.add_edge(str(ori), str(des))

    return graph


def experiment(graph):
    print('Graph info:')
    print(' - vertices:', len(graph.vertices()))
    print(' - edges:', len(graph.edges()))
    print()

    start_time = time.time()
    print('SAT solving - ')
    path = hamilton.find_hamiltonian_path(graph)
    print('Solving last: ', (time.time() - start_time), 'segs.')
    print('Checking correctness:', hamilton.check_correctness(graph, path))
    print(path)
    print('\n\n')

    # print('Backtrack solving - ')
    # start_time = time.time()
    # path = hamilton.backtrack_hamilton(graph, graph.vertices()[0])
    # print('Solving last: ', (time.time() - start_time), 'segs.')
    # print('Checking correctness:', hamilton.check_correctness(graph, path))
    # print('\n\n')


if __name__ == '__main__':
    graph_list = ['graphs/structured-type1-100nodes.txt']

    # for filename in graph_list:
    #     graph = Graph()
    #     graph.add_from_text(filename)
    #     experiment(graph)

    for n_vertices in range(100, 251, 75):
        for n_edges in range(100, 10000, 1000):
            graph = random_graph(n_vertices, n_edges)
            experiment(graph)

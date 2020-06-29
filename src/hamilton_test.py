import random
import time
from graph import Graph
import networkx as nx


def random_graph(n_vertices, n_edges):
    graph = Graph()
    for i in range(n_vertices):
        graph.add_vertex(str(i))

    while len(graph.edges()) < n_edges:
        ori = random.randint(0, n_vertices - 1)
        des = random.randint(0, n_vertices - 1)
        graph.add_edge(str(ori), str(des))

    return graph

def internet_hamilton(edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    F = [(G,[list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        print(len(F))
        graph,path = F.pop()
        confs = []
        for node in graph.neighbors(path[-1]):
            conf_p = path[:]
            conf_p.append(node)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return None

def experiment(graph):
    print('Graph info:')
    print(' - vertices:', len(graph.vertices()))
    print(' - edges:', len(graph.edges()))
    print()

    start_time = time.time()
    print('SAT solving - ')
    path = graph.find_hamiltonian_path()
    print('Solving last: ', (time.time() - start_time), 'segs.')
    #    print('Checking correctness:', check_correctness(graph, path))
    print(path)
    print('\n\n')

    print('Backtrack solving - ')
    start_time = time.time()
    path =     internet_hamilton(list(graph.edges()))
    print('Solving last: ', (time.time() - start_time), 'segs.')
    # print('Checking correctness:', hamilton.check_correctness(graph, path))
    print('\n\n')


if __name__ == '__main__':
    graph_list = [
        'graphs/structured-type1-100nodes.txt',
        'graphs/structured-type1-400nodes.txt',
        'graphs/structured-type1-900nodes.txt',
        'graphs/structured-type1-1600nodes.txt'
    ]

    for filename in graph_list:
        graph = Graph()
        graph.add_from_text(filename)
        experiment(graph)

    # for n_vertices in range(100, 251, 75):
    #     for n_edges in range(100, 10000, 1000):
    #         graph = random_graph(n_vertices, n_edges)
    #         experiment(graph)

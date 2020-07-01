"""
A simple Python Module, demonstrating the essential
facts and functionalities of graphs.

Implements a function find_hamiltonian_path
that reduces the problem to SAT.

We uses internally the CaDiCaL solver.
Improved from: https://www.python-course.eu/graphs_python.php
"""

import math
import random
from pysat.solvers import Solver
from pysat.card import CardEnc
from pysat.formula import IDPool
from SATreduce.utility import xvar



class Graph(dict):
    """
    Class that implements a directed graph. Inherited from
    dict data structure.
    """

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be use.
            Might raise ValueError exception.
        """
        if graph_dict is None:
            graph_dict = {}

        for k in graph_dict:
            if not isinstance(k, str):
                raise ValueError('Nodes should be identified with str')
            if not isinstance(graph_dict[k], set):
                raise ValueError('Destinies should be a set')

            for vertex in graph_dict[k]:
                if vertex not in graph_dict:
                    raise ValueError('Destinies should be a node.')

        super().__init__(graph_dict)

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.keys())

    def edges(self):
        """ returns the edges of a graph """
        return set(
            (origin, destiny) for origin, destiny in self.iterate_edges())

    def add_vertex(self, vertex):
        """ 
        If the vertex "vertex" is not in
        self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary.
        Otherwise nothing has to be done.
            
        Might raise ValueError exception.
        """
        if not isinstance(vertex, str):
            raise ValueError('Nodes should be identified with str')

        if vertex not in self:
            self[vertex] = set()

    def add_edge(self, ori, des):
        """
        Add a new edge to the graph. If the
        requires that nodes are of type str.
        
        Might raise ValueError exception.
        """

        if not isinstance(ori, str) or not isinstance(des, str):
            raise ValueError('Nodes should be identified with str')

        for vertex in [ori, des]:
            if vertex not in self:
                self[vertex] = set()

        self[ori].add(des)
        self[des].add(ori)

    def add_from_text(self, filename):
        """
        A method that read a graph from text.

        Format done as in http://wwwinfo.deis.unical.it/npdatalog/-
        experiments/hamiltoniancycle.htm

        Requires as param a file path
        """
        with open(filename) as file_:
            for line in file_:
                if line[0:4] == 'node':
                    self.add_vertex(line[5:-3])
                elif line[0:5] == 'start':
                    pass
                else:
                    formated_line = line[5:-3]
                    ori, des = formated_line.split(',')
                    self.add_edge(ori, des)

    def iterate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        for key, values in self.items():
            for vertex in values:
                yield (key, vertex)

    def __str__(self):
        res = "vertices: "

        for k in self:
            res += str(k) + " "
        res += "\nedges: "

        index = 1
        for edge in self.iterate_edges():
            res += str(edge) + " "
            if index % 4 == 0:
                res += "\n       "
            index += 1

        return res

    def find_hamiltonian_path(self, check_cycle=False, verbose=False):
        """
        should it exists, find a Hamiltonian on
        current self. Otherwise return empty list.
        """
        if not self.edges():
            return []

        if verbose:
            print('Codifying SAT Solver...')
        length = len(self.vertices())
        solver = Solver(name='cd')
        names = {}
        vpool = IDPool()

        for integer, vertex in enumerate(self.vertices()):
            names[integer + 1] = vertex
        names[0] = names[length]

        for position_in_path in range(length):
            for vertex in range(1, length + 1):
                vpool.id(xvar(vertex, position_in_path))
        if verbose:
            print(' -> Codifying: All Positions occupied')
        for position_in_path in range(length):
            var_list = [
                vpool.id(xvar(vertex, position_in_path))
                for vertex in range(1, length + 1)
            ]

            cnf = CardEnc.equals(lits=var_list, vpool=vpool)
            solver.append_formula(cnf)

        if verbose:
            print(' -> Codifying: All vertex visited')
        for vertex in range(1, length + 1):
            var_list = [
                vpool.id(xvar(vertex, position_in_path))
                for position_in_path in range(length)
            ]

            cnf = CardEnc.equals(lits=var_list, vpool=vpool)
            solver.append_formula(cnf)

        if verbose:
            print(' -> Codifying: Adjacency Matrix')
        edges = self.edges()
        for vertex_a in range(1, length + 1):
            for vertex_b in range(vertex_a + 1, length + 1):
                if (names[vertex_a], names[vertex_b]) not in edges:
                    for position_in_path in range(length - 1):
                        solver.add_clause([
                            -vpool.id(xvar(vertex_a, position_in_path)),
                            -vpool.id(xvar(vertex_b, position_in_path + 1)),
                        ])
                        solver.add_clause([
                            -vpool.id(xvar(vertex_b, position_in_path)),
                            -vpool.id(xvar(vertex_a, position_in_path + 1)),
                        ])

                    if check_cycle:
                        solver.add_clause([
                            vpool.id(xvar(vertex_b, length - 1)),
                            vpool.id(xvar(vertex_a, 0))
                        ])
                        solver.add_clause([
                            vpool.id(xvar(vertex_b, 0)),
                            vpool.id(xvar(vertex_a, length - 1))
                        ])

        if verbose:
            print('Running SAT Solver...')
        solution = []
        if solver.solve():
            for index, variable in enumerate(solver.get_model()):
                if variable > 0 and index < length**2:
                    solution.append(names[variable % length])

        return solution

    def coloring(self, n_color, verbose=True):
        """
        Returns whether or not there exists a vertex coloring
        of, at most, n_color colors.

        Accepts two params:
        - n_color: number of color to check
        - verbose: whether or not print the process

        Might raise ValueError exception.
        """
        if n_color < 0:
            raise ValueError('Number of colors must be positive integer')

        if n_color == 0:
            return not bool(self.vertices())

        if verbose:
            print('\nCodifying SAT Solver...')

        solver = Solver(name='cd')
        vpool = IDPool()

        if verbose:
            print(' -> Codifying: Every vertex must have a color, and only one')

        for vertex in self.vertices():
            cnf = CardEnc.equals(lits=[
                vpool.id('{}color{}'.format(vertex, color))
                for color in range(n_color)
            ],
                                 vpool=vpool,
                                 encoding=0)

            solver.append_formula(cnf)

        if verbose:
            print(' -> Codifying: No two neighbours can have the same color')

        for vertex in self.vertices():
            for neighbour in self[vertex]:
                for color in range(n_color):
                    solver.add_clause([
                        -vpool.id('{}color{}'.format(vertex, color)),
                        -vpool.id('{}color{}'.format(neighbour, color))
                    ])
        if verbose:
            print('Running SAT Solver...')
        return solver.solve()

    def minimun_coloring(self):
        """
        Using the minimizing trick, return the size
        of the minimun coloring. Use the function coloring
        """

        old = len(self)
        new = len(self) // 2

        while old != new:
            if self.coloring(new, False):
                old = new
                new = new // 2

            else:
                new += math.ceil((old - new) / 2)

        return new

    def dominating_subset(self, k=1, verbose=True):
        """
        Check if there exists a vertex cover of, at most, k-vertices.
        Accepts as params:
        - n_color: number of color to check
        - verbose: whether or not print the process
        """
        if not self.edges():
            return []

        if verbose:
            print('\nCodifying SAT Solver...')

        solver = Solver(name='cd')
        vpool = IDPool()
        vertices_ids = [vpool.id(vertex) for vertex in self.vertices()]

        if verbose:
            print(' -> Codifying: Every vertex must be accessible')

        for vertex in self.vertices():
            solver.add_clause(
                [vpool.id(vertex)] +
                [vpool.id(adjacent_vertex) for adjacent_vertex in self[vertex]])

        if verbose:
            print(' -> Codifying: At most', k, 'vertices should be selected')

        cnf = CardEnc.atmost(lits=vertices_ids, bound=k, vpool=vpool)
        solver.append_formula(cnf)

        if verbose:
            print('Running SAT Solver...')
        return solver.solve()

    def minimun_dominating_subset(self):
        """
        Using the minimizing trick, return the size
        of the minimun dominating subset.
        """
        old = len(self)
        new = len(self) // 2

        while old != new:
            if self.dominating_subset(new, False):
                old = new
                new = new // 2

            else:
                new += math.ceil((old - new) / 2)

        return new

    def random_graph(n_vertices, n_edges):
        """
        Class method that returns a random graph.

        Receives two params:
        n_vertices: the number of vertices
        n_edges: the number of edges.

        """

        graph = Graph()
        for i in range(n_vertices):
            graph.add_vertex(str(i))

        for i in range(n_edges):
            ori = random.randint(0, n_vertices - 1)
            des = random.randint(0, n_vertices - 1)
            graph.add_edge(str(ori), str(des))

        return graph

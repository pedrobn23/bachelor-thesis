"""
A simple Python Module, demonstrating the essential
facts and functionalities of graphs.

Improved from: https://www.python-course.eu/graphs_python.php
"""


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
        """ If the vertex "vertex" is not in
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

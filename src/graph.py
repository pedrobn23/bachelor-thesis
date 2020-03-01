""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""

class Graph(dict):
    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be use.
            Might raise ValueError exception.
        """
        if graph_dict == None:
            graph_dict = {}

        for k in graph_dict:
            if not isinstance(k, str):
                raise ValueError('Nodes should be identified with str')
            if not isinstance(graph_dict[k], list):
                raise ValueError('Destinies should be a list')
            else:
                for v in graph_dict[k]:
                    if v not in graph_dict:
                        raise ValueError('Destinies should be a node.')

        super().__init__(graph_dict)

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.keys())

    def edges(self):
        """ returns the edges of a graph """
        return [(origin, destiny) for origin, destiny in self.iterate_edges()]

    def is_totally_isolated(self):
        """ returns if the graph is totally isolated """
        for a in self:
            if self[a] != []:
                return False
        return True

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
            self[vertex] = []

    def add_edge(self, ori, des):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges! TBD: SOLVE THIS
        """
        if not isinstance(ori, str) or not isinstance(des, str):
            raise ValueError('Nodes should be identified with str')

        if ori in self:
            self[ori].append(des)
        else:
            self[ori] = [des]

    def iterate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        for key, values in self.items():
            for v in values:
                yield (key, v)

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

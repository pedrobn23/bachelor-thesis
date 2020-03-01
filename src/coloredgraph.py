from graph import Graph

class ColoredGraph(Graph):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        super().__init__(graph_dict)

        self.color_dict = {k : 0 for k in self}

    def add_vertex(self, vertex):
        super().add_vertex()
        self.color_dict[vertex] = 0

    def paint_vertex(self, vertex, color):
        if vertex not in self:
            raise ValueError('Not a vertex')

        self.color_dict[vertex] = color

    def vertex_color(self, vertex):
        if vertex not in self:
            raise ValueError('Not a vertex')

        return self.color_dict[vertex]


    def check_correctly_colored()

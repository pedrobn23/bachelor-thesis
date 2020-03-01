# utils_test.py
from unittest import TestCase, main
from graph import Graph

class GraphTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        g = { "a" : ["d"],
              "b" : ["c"],
              "c" : ["b", "c", "d", "e"],
              "d" : ["a", "c"],
              "e" : ["c"],
              "f" : []
        }

        self.graph = Graph(g)

    def test_vertices(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f'], self.graph.vertices())

    def test_graph(self):
        self.assertEqual(
            [('a', 'd'), ('b', 'c'), ('c', 'b'), ('c', 'c'), ('c', 'd'),
             ('c', 'e'), ('d', 'a'), ('d', 'c'), ('e', 'c')],
            self.graph.edges())

    def test_add_vertex(self):
        self.graph.add_vertex('z')
        self.assertTrue('z' in self.graph.vertices())

    def test_add_edge(self):
        self.graph.add_edge('x','y')
        self.assertTrue(('x', 'y') in self.graph.edges() )

    def test_totally_isolated(self):
        ge = Graph({'a':[],'b':[]})
        self.assertTrue(ge.is_totally_isolated())

if __name__ == '__main__':
    main()


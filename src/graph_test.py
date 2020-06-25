"""
Module that implements automatic test cases for
Graph class.
"""

from unittest import TestCase, main
from graph import Graph


class GraphTestCase(TestCase):
    """
    Test Class for Graph class.
    """

    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        graph = {
            "a": {"d"},
            "b": {"c"},
            "c": {"b", "c", "d", "e"},
            "d": {"a", "c"},
            "e": {"c"},
            "f": set()
        }

        graph2 = {"a": {"b", "c"}, "b": {"c", "a"}, "c": {"b", "a"}}

        self.graph = Graph(graph)
        self.graph2 = Graph(graph2)

    def test_vertices(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f'], self.graph.vertices())

    def test_graph(self):
        self.assertEqual(
            {('a', 'd'), ('b', 'c'), ('c', 'b'), ('c', 'c'), ('c', 'd'),
             ('c', 'e'), ('d', 'a'), ('d', 'c'), ('e', 'c')},
            self.graph.edges())

    def test_add_vertex(self):
        self.graph.add_vertex('z')
        self.assertTrue('z' in self.graph.vertices())

    def test_add_edge(self):
        self.graph.add_edge('x', 'y')
        self.assertTrue(('x', 'y') in self.graph.edges())


if __name__ == '__main__':
    main()

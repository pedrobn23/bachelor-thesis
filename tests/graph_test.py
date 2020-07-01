"""
Module that implements automatic test cases for
Graph class.
"""

from unittest import TestCase, main
from src import graph


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

    def check_correctness(graph, path):
        if path:
            length = len(graph)
            for i in range(length - 1):
                if path[(i + 1)] not in graph[path[i]]:
                    return False
        return True

    def test_hamilton(self):
        self.assertEqual(
            self.graph.find_hamiltonian_path(check_cycle=True, verbose=False),
            [])

        path2 = self.graph2.find_hamiltonian_path(check_cycle=True,
                                                  verbose=False)

        self.assertTrue(GraphTestCase.check_correctness(self.graph2, path2))

    def test_coloring(self):
        self.assertTrue(not self.graph2.coloring(2, verbose=False))
        self.assertEqual(self.graph2.minimun_coloring(), 3)

    def test_domin(self):
        self.assertTrue(self.graph2.dominating_subset(1, verbose=False))
        self.assertEqual(self.graph2.minimun_dominating_subset(), 1)


if __name__ == '__main__':
    main()

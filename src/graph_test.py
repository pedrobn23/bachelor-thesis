# utils_test.py
from unittest import TestCase, main
from graph import Graph


class GraphTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        g = {
            "a": {"d"},
            "b": {"c"},
            "c": {"b", "c", "d", "e"},
            "d": {"a", "c"},
            "e": {"c"},
            "f": set()
        }

        g2 = {"a": {"b", "c"}, "b": {"c", "a"}, "c": {"b", "a"}}

        self.graph = Graph(g)
        self.graph2 = Graph(g2)

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

    def test_add_from_text(self):
        
        
    def test_hamiltonian_path(self):
        self.assertTrue(self.graph2.find_hamiltonian_path(
        ) in [["a", "b", "c", "a"], ["a", "c", "b", "a"], ["b", "c", "a", "b"],
              ["b", "a", "c", "b"], ["c", "a", "b", "c"], ["c", "b", "a", "c"]])
        self.assertTrue(not self.graph.find_hamiltonian_path())


if __name__ == '__main__':
    main()

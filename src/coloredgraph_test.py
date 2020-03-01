from unittest import TestCase, main
from coloredgraph import ColoredGraph

class ColoredGraphTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        g = { "a" : ["d"],
              "b" : ["c"],
              "c" : ["b", "c", "d", "e"],
              "d" : ["a", "c"],
              "e" : ["c"],
              "f" : []
        }

        self.colorGraph = ColoredGraph(g)

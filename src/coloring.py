import time
import math
import random

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF



def minimun_coloring(graph):
    old = len(graph)
    new = len(graph) // 2

    while old != new:
        if coloring(graph, new, False):
            old = new
            new = new // 2

        else:
            new += math.ceil((old - new) / 2)

    return new

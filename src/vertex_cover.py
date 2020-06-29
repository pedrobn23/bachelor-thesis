import time
import math
import random

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF, CNFPlus






rg = random_graph(19, 5)
graph = Graph(rg)
print(rg)
print(minimun_cover(graph))

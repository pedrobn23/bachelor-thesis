import time
import math
import random
import copy

from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool, CNF


class NaiveQBF():
    def __init__(self):
        self.formula = CNF
        self.quantifiers = []
        self.propagate = []

    def solve(self):
        return __solve(self.quantifiers, self.formula, self.propagate)

    def append_formula(self, formula):
        for clause in append_formula:
            self.formula.add_clause(clause)

    def propagate(self, variable):
        self.propagate.append(variable)
        if variable in self.quantifiers:
            self.quantifiers.remove(variable)

    def add_clause(self, clause):
        self.formula.add_clause(clause)

    def add_quantifiers(self, quantifier):
        if quantifier in self.quantifiers:
            raise ValueError('A variable can not be quantified twice')

        self.quantifiers.append(quantifier)

    def negate(self):
        self.formula = self.formula.negate()
        self.quantifiers = [-quant for quant in self.quantifiers]
        
    def __solve(quantifiers, formula, propagate):
        if quantifiers:
            new_quant = copy.deepcopy(quantifiers)
            quantifier = new_quant.pop()

            if quantifier < 0:
                return __solve(
                    new_quant, formula, propagate + [quantifier]) and __solve(
                        new_quant, formula, propagate + [-quantifier])
            else:
                if __solve(new_quant, formula, propagate + [quantifier]):
                    return True
                return __solve(new_quant, formula, propagate + [quantifier])
        else:
            solver = Solver(name='cd')
            solver.append_formula(self.cnf)
            return solver.solve()


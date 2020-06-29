"""
Module that implements QBF resolution
"""
import copy
from graph import Graph
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import CNF


class NaiveQBF():
    """
    This class work as a skeleton in order to defin qbf solver based on SAT.
    """   
    def __init__(self):
        """
        Constructor of the class. Always create an empty solver
        """
        self.formula = CNF()
        self.quantifiers = []
        self.propagate = []

    def append_formula(self, formula):
        """
        Append a formula (seen as a list of clauses) to the solver.
        """
        for clause in formula:
            self.formula.add_clause(clause)

    def propagate_literal(self, variable):
        """
        Add a literal to be propagated.
        """
        self.propagate.append(variable)
        if variable in self.quantifiers:
            self.quantifiers.remove(variable)

    def add_clause(self, clause):
        """
        Add a clause to the formula
        """

        self.formula.add_clause(clause)

    def add_quantifiers(self, quantifier):
        """
        Add a quantifier to the quantifiers list.
        Quantifiers are represented as integers. A positive
        quantifiers is interpreted as an exists, as well as
        a negative quantifiers is interpreted as a for all.
        """

        if quantifier in self.quantifiers:
            raise ValueError('A variable can not be quantified twice')

        self.quantifiers.append(quantifier)

    def negate(self):
        """
        negate the formula along with the quantifiers list.
        """
        self.formula = self.formula.negate()
        self.quantifiers = [-quant for quant in self.quantifiers]

    def __solve(quantifiers, formula, propagate):
        """
        Private method that implements the recursión that solve the problem.
        """
        if quantifiers:
            new_quant = copy.deepcopy(quantifiers)
            quantifier = new_quant.pop()

            if quantifier < 0:
                return NaiveQBF.__solve(
                    new_quant, formula, propagate + [quantifier]) and NaiveQBF.__solve(
                        new_quant, formula, propagate + [-quantifier])
            else:
                if NaiveQBF.__solve(new_quant, formula, propagate + [quantifier]):
                    return True
                return NaiveQBF.__solve(new_quant, formula, propagate + [quantifier])
        else:
            solver = Solver(name='cd')
            solver.append_formula(self.cnf)
            return solver.solve()
    def solve(self):
        """
        Solved the associated formula.
        """
        return NaiveQBF.__solve(self.quantifiers, self.formula, self.propagate)

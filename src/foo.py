from pysat.solvers import Glucose3
g = Glucose3()
g.add_clause([-1, 2])
g.add_clause([-2, 3])
print g.solve()
print g.get_model()


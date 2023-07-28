from csp import *

p = Problem()
p.add_variable(Variable("var1", [8, 8]))
p.add_variable(Variable("var2", [2, 17]))
p.add_variable(Variable("var3", [3, 2]))
p.add_constraint(AllDifferentConstraint(["var1", "var2"]))
p.add_constraint(AllEqualConstraint(["var2", "var3"]))

print(p.get_solutions())

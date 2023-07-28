from csp import *

problem = Problem()

# Add variables to the problem
alice = Variable("bob", ["beach", "hiking", "stay home"])
bob = Variable("Mouhanned", ["beach", "hiking", "stay home"])
charlie = Variable("giraffe!?", ["beach", "hiking", "stay home"])
problem.add_variable(alice)
problem.add_variable(bob)
problem.add_variable(charlie)

# Add constraints to the problem
problem.add_constraint(AllDifferentConstraint(["bob", "Mouhanned", "giraffe!?"]))

# Get solutions to the problem
solutions = problem.get_solutions()
print(solutions)

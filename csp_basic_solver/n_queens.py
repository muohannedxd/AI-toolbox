from csp import *

# Create a Problem instance
n_queens_problem = Problem()

# Define the number of queens and board size
n = 8

# Define variables representing each column and their domains (row positions)
variables = []
for col in range(n):
    variable_name = f"column_{col}"
    variable_domain = list(range(n))
    column_variable = Variable(variable_name, variable_domain)
    n_queens_problem.add_variable(column_variable)
    variables.append(column_variable)

# Add constraints to enforce no two queens threatening each other
constraints = []
for i in range(n):
    for j in range(i + 1, n):
        constraints.append(Constraint([f"column_{i}", f"column_{j}"]))

# Diagonal constraints
for i in range(n):
    for j in range(i + 1, n):
        constraints.append(Constraint([f"column_{i}", f"column_{j}"], lambda values: abs(values[0] - values[1]) != j - i))

for constraint in constraints:
    n_queens_problem.add_constraint(constraint)

# Solve the problem and print the solutions
solutions = n_queens_problem.get_solutions()
print(solutions)
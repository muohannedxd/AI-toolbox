from csp import Problem, Variable, AllDifferentConstraint

# Create a new CSP problem instance
problem = Problem()

# Define variables
variables = [
    Variable("A", [1, 2, 3]),  # Variable 'A' with domain [1, 2, 3]
    Variable("B", [4, 5]),     # Variable 'B' with domain [4, 5]
    Variable("C", [1, 2]),     # Variable 'C' with domain [1, 2]
]

# Add variables to the problem
for variable in variables:
    problem.add_variable(variable)

# Define constraints
constraint1 = AllDifferentConstraint(["A", "B"])  # Constraint: A and B must have different values
constraint2 = AllDifferentConstraint(["B", "C"])  # Constraint: B and C must have different values

# Add constraints to the problem
problem.add_constraint(constraint1)
problem.add_constraint(constraint2)

# Solve the problem and get all solutions
solutions = problem.get_solutions()

# Print the solutions
for solution in solutions:
    print(solution)
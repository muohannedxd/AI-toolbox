from typing import Dict, List


class Variable:
    def __init__(self, name: str, domain: List[int]):
        self.name = name
        self.domain = domain


class Constraint:
    def __init__(self, variables: List[str]):
        self.variables = variables

    def check(self, values: List[int]) -> bool:
        return True


class AllDifferentConstraint(Constraint):
    def check(self, values: List[int]) -> bool:
        return len(values) == len(set(values))


class AllEqualConstraint(Constraint):
    def check(self, values: List[int]) -> bool:
        return all(val == values[0] for val in values)


def filter_dictionary(d: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    return {k: v for k, v in d.items() if k in keys}


def dictionary_to_array(d: Dict[str, int]) -> List[int]:
    return list(d.values())


def union(d1: Dict[str, int], d2: Dict[str, int]) -> Dict[str, int]:
    return {**d1, **d2}


def union_arr(a: List[int], b: List[int]) -> List[int]:
    return list(set(a) | set(b))


class Problem:
    def __init__(self):
        self.variables: List[Variable] = []
        self.constraints: List[Constraint] = []

    def add_variable(self, variable: Variable) -> None:
        """
        Add a variable to the problem.

        Args:
            variable: The variable to add.
        """
        self.variables.append(variable)

    def add_constraint(self, constraint: Constraint) -> None:
        """
        Add a constraint to the problem.

        Args:
            constraint: The constraint to add.
        """
        self.constraints.append(constraint)

    def check_consistency(self, assignment: Dict[str, int]) -> bool:
        """
        Check if an assignment is consistent with the problem's constraints.

        Args:
            assignment: The assignment to check.

        Returns:
            True if the assignment is consistent, False otherwise.
        """
        for constraint in self.constraints:
            relevant_values = filter_dictionary(assignment, constraint.variables)
            if not constraint.check(dictionary_to_array(relevant_values)):
                return False
        return True

    def find(self, assignment: Dict[str, int], variables: List[Variable]) -> List[Dict[str, int]]:
        """
        Find all solutions to the problem.

        Args:
            assignment: The current assignment.
            variables: The remaining variables to assign.

        Returns:
            A list of all solutions to the problem.
        """
        if not variables:
            return [assignment]

        var = variables[0]
        remaining_vars = variables[1:]
        results = []
        for option in var.domain:
            new_assignment = union(assignment, {var.name: option})
            if self.check_consistency(new_assignment):
                results.extend(self.find(new_assignment, remaining_vars))
        return results

    def get_solutions(self) -> List[Dict[str, int]]:
        """
        Get all solutions to the problem.

        Returns:
            A list of all solutions to the problem.
        """
        return self.find({}, self.variables.copy())
from typing import Dict, List


class Variable:
    def __init__(self, name: str, domain: List[int]):
        self.name = name
        self.domain = domain


class Constraint:
    def __init__(self, variables: List[str]):
        self.variables = variables

    def check(self, values: List[int]) -> bool:
        return True

class AtMostConstraint(Constraint):
    def __init__(self, variables: List[str], max_val: int):
        super().__init__(variables)
        self.max_val = max_val

    def check(self, values: List[int]) -> bool:
        return len([val for val in values if val is not None]) <= self.max_val


class AtMostConstraint(Constraint):
    def __init__(self, variables: List[str], max_val: int):
        super().__init__(variables)
        self.max_val = max_val

    def check(self, values: List[int]) -> bool:
        count = 0
        for val in values:
            if val is not None:
                count += 1
                if count > self.max_val:
                    return False
        return True


class AtLeastConstraint(Constraint):
    def __init__(self, variables: List[str], min_val: int):
        super().__init__(variables)
        self.min_val = min_val

    def check(self, values: List[int]) -> bool:
        count = 0
        for val in values:
            if val is not None:
                count += 1
        return count >= self.min_val


class AllDifferentConstraint(Constraint):
    def check(self, values: List[int]) -> bool:
        return len(values) == len(set(values))


class AllEqualConstraint(Constraint):
    def check(self, values: List[int]) -> bool:
        return all(val == values[0] for val in values)


def filter_dictionary(d: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    return {k: v for k, v in d.items() if k in keys}


def dictionary_to_array(d: Dict[str, int]) -> List[int]:
    return list(d.values())


def union(d1: Dict[str, int], d2: Dict[str, int]) -> Dict[str, int]:
    return {**d1, **d2}


def union_arr(a: List[int], b: List[int]) -> List[int]:
    return list(set(a) | set(b))


class Problem:
    def __init__(self):
        self.variables: List[Variable] = []
        self.constraints: List[Constraint] = []

    def add_variable(self, variable: Variable) -> None:
        """
        Add a variable to the problem.

        Args:
            variable: The variable to add.
        """
        self.variables.append(variable)

    def add_constraint(self, constraint: Constraint) -> None:
        """
        Add a constraint to the problem.

        Args:
            constraint: The constraint to add.
        """
        self.constraints.append(constraint)

    def check_consistency(self, assignment: Dict[str, int]) -> bool:
        """
        Check if an assignment is consistent with the problem's constraints.

        Args:
            assignment: The assignment to check.

        Returns:
            True if the assignment is consistent, False otherwise.
        """
        for constraint in self.constraints:
            relevant_values = filter_dictionary(assignment, constraint.variables)
            if not constraint.check(dictionary_to_array(relevant_values)):
                return False
        return True

    def find(self, assignment: Dict[str, int], variables: List[Variable]) -> List[Dict[str, int]]:
        """
        Find all solutions to the problem.

        Args:
            assignment: The current assignment.
            variables: The remaining variables to assign.

        Returns:
            A list of all solutions to the problem.
        """
        if not variables:
            return [assignment]

        var = variables[0]
        remaining_vars = variables[1:]
        results = []
        for option in var.domain:
            new_assignment = union(assignment, {var.name: option})
            if self.check_consistency(new_assignment):
                results.extend(self.find(new_assignment, remaining_vars))
        return results

    def get_solutions(self) -> List[Dict[str, int]]:
        """
        Get all solutions to the problem.

        Returns:
            A list of all solutions to the problem.
        """
        return self.find({}, self.variables.copy())

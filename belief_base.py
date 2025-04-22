
from sympy import symbols
from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable
from sympy.parsing.sympy_parser import parse_expr

class BeliefBase:
    def __init__(self):
        self.beliefs = set()

    def _parse(self, formula_str):
        '''
        Parse a string formula into a sympy logical expression.
        Example: "A & B" -> sympy expression A & B
        '''
        try:
            return parse_expr(formula_str, evaluate=False)
        except Exception as e:
            raise ValueError(f"Failed to parse formula '{formula_str}': {e}")

    def add_belief(self, formula_str):
        '''
        Add a belief (string format).
        '''
        parsed = self._parse(formula_str)
        self.beliefs.add(parsed)

    def remove_belief(self, formula_str):
        '''
        Remove a belief (string format).
        '''
        parsed = self._parse(formula_str)
        if parsed in self.beliefs:
            self.beliefs.remove(parsed)

    def display_beliefs(self):
        '''
        Display all current beliefs.
        '''
        print("Current belief base:")
        for belief in self.beliefs:
            print("-", belief)

    def is_consistent(self):
        '''
        Check whether the belief base is logically consistent.
        Uses sympy's satisfiable() function.
        '''
        if not self.beliefs:
            return True
        conjunction = None
        for b in self.beliefs:
            conjunction = b if conjunction is None else (conjunction & b)
        return bool(satisfiable(to_cnf(conjunction, simplify=True)))

    def get_beliefs(self):
        '''
        Return the set of beliefs (for use in other modules).
        '''
        return self.beliefs

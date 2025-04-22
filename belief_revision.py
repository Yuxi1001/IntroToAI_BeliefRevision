
from itertools import chain, combinations
from resolution import pl_resolution

def powerset(s):
    """Return all subsets of a set s (powerset)."""
    s = list(s)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def is_consistent(subset):
    """A belief set is consistent if it does NOT entail a contradiction."""
    return not pl_resolution(subset, 'False')  # check if subset ⊨ False

def revise(belief_base, new_formula_str):
    """
    Partial Meet Revision using resolution-based consistency check.
    Input:
        belief_base: BeliefBase object with .get_beliefs()
        new_formula_str: φ, the new formula to add
    Output:
        Revised belief base with φ integrated
    """
    original_beliefs = set(map(str, belief_base.get_beliefs()))
    new_formula_str = str(new_formula_str)
    # original_beliefs = belief_base.get_beliefs()

    # Step 1: find all subsets consistent with φ
    valid_subsets = []
    for subset in powerset(original_beliefs):
        subset = set(subset)
        if is_consistent(subset | {new_formula_str}):
            valid_subsets.append(subset)

    # Step 2: choose maximal consistent subset
    if not valid_subsets:
        new_beliefs = {new_formula_str}
    else:
        max_subset = max(valid_subsets, key=len)
        new_beliefs = set(max_subset)
        new_beliefs.add(new_formula_str)

    belief_base.beliefs = new_beliefs
    return belief_base

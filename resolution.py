
from itertools import product

def parse_clause(expr):
    """Convert a string like 'A | ~B' into a set: {'A', '~B'}"""
    return set(map(str.strip, expr.split('|')))

def negate(expr):
    """Negate a single literal or a compound formula (assume only atoms or ~atoms)"""
    if expr.startswith('~'):
        return expr[1:]
    return '~' + expr

def pl_resolution(kb_clauses, query):
    """
    Resolution algorithm.
    kb_clauses: set of strings, each string is a clause (e.g. 'A | B')
    query: string (e.g. 'C'), the formula to be entailed
    Returns True if kb entails query
    """
    # Convert to set of clauses
    clauses = [parse_clause(cl) for cl in kb_clauses]
    clauses.append({negate(query)})  # add ¬query

    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = pl_resolve(ci, cj)
            if set() in resolvents:
                return True  # empty clause derived
            new.update(resolvents)
        if new.issubset(set(map(frozenset, clauses))):
            return False  # no progress
        for c in new:
            if c not in clauses:
                clauses.append(set(c))

def pl_resolve(ci, cj):
    """Return resolvents of two clauses (sets of literals)"""
    resolvents = set()
    for di in ci:
        for dj in cj:
            if di == negate(dj):
                resolvent = (ci - {di}) | (cj - {dj})
                resolvents.add(frozenset(resolvent))
    return resolvents

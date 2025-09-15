# map_coloring_csp.py
# CSP Map Coloring using backtracking + MRV + Forward Checking

from copy import deepcopy

def select_unassigned_variable(assignment, domains):
    """MRV: choose the unassigned variable with smallest domain."""
    unassigned = [v for v in domains.keys() if v not in assignment]
    # sort by domain size, tie-breaker lexicographic
    return min(unassigned, key=lambda v: (len(domains[v]), v)) if unassigned else None

def is_consistent(var, value, assignment, neighbors):
    """Check if assigning value to var conflicts with already assigned neighbors."""
    for n in neighbors[var]:
        if n in assignment and assignment[n] == value:
            return False
    return True

def forward_check(var, value, domains, neighbors):
    """
    Do forward checking: remove 'value' from domains of unassigned neighbors.
    Return a dict of {neighbor: [removed_values]} to allow restoration, or None if any domain becomes empty.
    """
    removed = {}
    for n in neighbors[var]:
        if value in domains[n]:
            # remove temporarily
            domains[n].remove(value)
            removed.setdefault(n, []).append(value)
            if len(domains[n]) == 0:
                # failure, restore before returning None
                for rn, vals in removed.items():
                    domains[rn].extend(vals)
                return None
    return removed

def restore_domains(domains, removed):
    """Restore values removed during forward checking."""
    if not removed:
        return
    for var, vals in removed.items():
        domains[var].extend(vals)

def backtrack(assignment, domains, neighbors):
    # If assignment is complete
    if len(assignment) == len(domains):
        return assignment

    var = select_unassigned_variable(assignment, domains)
    if var is None:
        return None

    # Try values in domain (no special ordering)
    for value in list(domains[var]):  # list() to iterate over a snapshot
        if is_consistent(var, value, assignment, neighbors):
            # assign
            assignment[var] = value
            # deep copy not needed for domains if we restore after
            removed = forward_check(var, value, domains, neighbors)
            if removed is not None:
                result = backtrack(assignment, domains, neighbors)
                if result is not None:
                    return result
            # undo
            restore_domains(domains, removed)
            del assignment[var]
    return None

def solve_map_coloring(variables, neighbors, colors):
    # domains: dict var -> list(colors)
    domains = {v: list(colors) for v in variables}
    solution = backtrack({}, domains, neighbors)
    return solution

if __name__ == "__main__":
    # Example: Australia map
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q' : ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW', 'T'],   # sometimes T is considered separate; include for completeness
        'T': ['V']
    }
    colors = ['red', 'green', 'blue']

    solution = solve_map_coloring(variables, neighbors, colors)
    if solution:
        print("Solution found:")
        for region in sorted(solution):
            print(f"  {region} -> {solution[region]}")
    else:
        print("No solution found with given colors.")

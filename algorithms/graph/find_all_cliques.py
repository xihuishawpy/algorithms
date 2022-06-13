"""
Finds all cliques in an undirected graph. A clique is a set of vertices in the
graph such that the subgraph is fully connected (ie. for any pair of nodes in
the subgraph there is an edge between them).
"""

def find_all_cliques(edges):
    """
    takes dict of sets
    each key is a vertex
    value is set of all edges connected to vertex
    returns list of lists (each sub list is a maximal clique)
    implementation of the basic algorithm described in:
    Bron, Coen; Kerbosch, Joep (1973), "Algorithm 457: finding all cliques of an undirected graph",
    """

    def expand_clique(candidates, nays):
        nonlocal compsub
        if candidates or nays:
            for selected in candidates.copy():
                candidates.remove(selected)
                candidates_temp = get_connected(selected, candidates)
                nays_temp = get_connected(selected, nays)
                compsub.append(selected)
                expand_clique(candidates_temp, nays_temp)
                nays.add(compsub.pop())

        else:
            nonlocal solutions
            solutions.append(compsub.copy())

    def get_connected(vertex, old_set):
        return {neighbor for neighbor in edges[str(vertex)] if neighbor in old_set}

    compsub = []
    solutions = []
    possibles = set(edges.keys())
    expand_clique(possibles, set())
    return solutions

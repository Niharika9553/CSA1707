# Depth First Search implementation in Python

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(graph, neighbour, visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# Run DFS
print("DFS Traversal starting from A:")
dfs(graph, 'A')

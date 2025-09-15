import heapq

# A* Algorithm Implementation
def a_star(graph, start, goal, heuristic):
    # Priority queue: stores (f, g, current_node, path)
    open_list = []
    heapq.heappush(open_list, (0, 0, start, [start]))

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print(f"Path found: {' -> '.join(path)} with cost {g}")
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]  # f = g + h
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    print("No path found.")

# Example Graph (Weighted)
# Each node has neighbors with travel cost
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values (estimated cost from each node to goal G)
heuristic = {
    'A': 4, 'B': 3, 'C': 5,
    'D': 2, 'E': 1, 'F': 2, 'G': 0
}

# Run A* Search
a_star(graph, 'A', 'G', heuristic)

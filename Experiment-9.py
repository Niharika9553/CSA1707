import itertools

# Distance matrix for 4 cities (A, B, C, D)
# distance[i][j] = distance from city i to city j
distance = [
    [0, 10, 15, 20],  # A
    [10, 0, 35, 25],  # B
    [15, 35, 0, 30],  # C
    [20, 25, 30, 0]   # D
]

cities = [0, 1, 2, 3]  # 0=A, 1=B, 2=C, 3=D
min_cost = float('inf')
best_path = None

# Try all possible city visit orders (permutations)
for perm in itertools.permutations(cities):
    cost = 0
    for i in range(len(perm) - 1):
        cost += distance[perm[i]][perm[i+1]]
    cost += distance[perm[-1]][perm[0]]  # return to start

    if cost < min_cost:
        min_cost = cost
        best_path = perm

# Show result
city_names = ['A', 'B', 'C', 'D']
path_str = " -> ".join(city_names[i] for i in best_path)
print("Travelling Salesman Problem Solution")
print(f"Shortest Path: {path_str} -> {city_names[best_path[0]]}")
print(f"Minimum Cost: {min_cost}")

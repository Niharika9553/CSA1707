from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    queue.append((0, 0, []))  # Start with both jugs empty

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        current_path = path + [(jug1, jug2)]

        if jug1 == target or jug2 == target:
            print(" Solution Found!\n")
            print("Steps:")
            for i, (a, b) in enumerate(current_path):
                print(f"Step {i}: Jug 1 = {a} | Jug 2 = {b}")
            return

        
            next_states = [
            (jug1_capacity, jug2),  # Fill Jug 1
            (jug1, jug2_capacity),  # Fill Jug 2
            (0, jug2),              # Empty Jug 1
            (jug1, 0),              # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug 2 -> Jug 1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], current_path))

    print(" No solution found.")
try:
    jug1_capacity = int(input("Enter the capacity of Jug 1: "))
    jug2_capacity = int(input("Enter the capacity of Jug 2: "))
    target = int(input("Enter the target amount to measure: "))

    if target > max(jug1_capacity, jug2_capacity):
        print(" Target cannot be more than the capacity of the largest jug.")
    else:
        water_jug_bfs(jug1_capacity, jug2_capacity, target)

except ValueError:
    print(" Please enter valid integers.")

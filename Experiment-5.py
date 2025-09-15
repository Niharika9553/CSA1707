from collections import deque

# Check if state is valid
def is_valid(m_left, c_left, m_right, c_right):
    # Missionaries should never be outnumbered by cannibals
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True

# BFS to solve Missionaries and Cannibals
def solve_missionaries_cannibals(m, c):
    start = (m, c, 1)  # (missionaries_left, cannibals_left, boat_side[1=left,0=right])
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (m_left, c_left, boat), path = queue.popleft()
        
        # Goal reached
        if (m_left, c_left, boat) == goal:
            return path

        # Possible moves (M, C)
        moves = [(2, 0), (0, 2), (1, 0), (0, 1), (1, 1)]

        for m_move, c_move in moves:
            if boat == 1:  # Boat on left -> move people to right
                new_m_left = m_left - m_move
                new_c_left = c_left - c_move
                new_m_right = m - new_m_left
                new_c_right = c - new_c_left
                new_boat = 0
            else:  # Boat on right -> move people back to left
                new_m_left = m_left + m_move
                new_c_left = c_left + c_move
                new_m_right = m - new_m_left
                new_c_right = c - new_c_left
                new_boat = 1

            new_state = (new_m_left, new_c_left, new_boat)

            if (0 <= new_m_left <= m and 0 <= new_c_left <= c and
                is_valid(new_m_left, new_c_left, new_m_right, new_c_right) and
                new_state not in visited):
                
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

# Main Program
if __name__ == "__main__":
    m = int(input("Enter no of missionaries: "))
    c = int(input("Enter no of cannibals: "))

    result = solve_missionaries_cannibals(m, c)

    if result:
        for step in result:
            print(step)
    else:
        print("No solution found.")

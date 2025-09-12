import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None, depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.zero_pos = board.index(0)
        self.cost = 0  # f = g + h
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def get_moves(self):
        moves = []
        x = self.zero_pos // 3
        y = self.zero_pos % 3
        
        # Possible moves: Up, Down, Left, Right
        directions = {'Up': (x - 1, y), 'Down': (x + 1, y), 'Left': (x, y - 1), 'Right': (x, y + 1)}
        
        for move, (new_x, new_y) in directions.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_pos = new_x * 3 + new_y
                new_board = list(self.board)
                # Swap zero with the target tile
                new_board[self.zero_pos], new_board[new_pos] = new_board[new_pos], new_board[self.zero_pos]
                moves.append(PuzzleState(tuple(new_board), self, move, self.depth + 1))
        return moves
    
    def manhattan_distance(self, goal):
        distance = 0
        for i in range(1, 9):
            current_index = self.board.index(i)
            goal_index = goal.index(i)
            current_x, current_y = current_index // 3, current_index % 3
            goal_x, goal_y = goal_index // 3, goal_index % 3
            distance += abs(current_x - goal_x) + abs(current_y - goal_y)
        return distance

def a_star(start, goal):
    open_list = []
    closed_set = set()
    
    start_state = PuzzleState(start)
    start_state.cost = start_state.manhattan_distance(goal)
    heapq.heappush(open_list, start_state)
    
    while open_list:
        current_state = heapq.heappop(open_list)
        
        if current_state.board == goal:
            return current_state
        
        closed_set.add(current_state.board)
        
        for neighbor in current_state.get_moves():
            if neighbor.board in closed_set:
                continue
            neighbor.cost = neighbor.depth + neighbor.manhattan_distance(goal)
            
            # Check if neighbor is already in open_list with higher cost
            for open_state in open_list:
                if neighbor.board == open_state.board and neighbor.cost >= open_state.cost:
                    break
            else:
                heapq.heappush(open_list, neighbor)
    
    return None

def print_solution(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    for step in path:
        print_board(step.board)
        if step.move:
            print("Move:", step.move)
        print()

def print_board(board):
    for i in range(3):
        print(board[3*i], board[3*i + 1], board[3*i + 2])

if __name__ == "__main__":
    # Example initial state (solvable)
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)
    
    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)
    
    solution = a_star(start, goal)
    if solution:
        print("Solution found in", solution.depth, "moves:\n")
        print_solution(solution)
    else:
        print("No solution found.")


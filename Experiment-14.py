import math

# Alpha-Beta Pruning function
def alpha_beta_pruning(depth, node_index, is_maximizing, values, alpha, beta):
    # Terminal condition: leaf node
    if depth == 3:  # since we have 8 leaf nodes -> depth = 3 (binary tree)
        return values[node_index]

    if is_maximizing:
        best = -math.inf
        for i in range(2):  # two children
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off
        return best

# Leaf nodes
values = [3, 5, 6, 9, 1, 2, 0, -1]

print("Leaf Nodes =", values)
optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
print("The Optimal Value is:", optimal_value)

import math

MAX, MIN = 1000, -1000


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, base_case) -> int:
    """
    Calculates the best move for the computer using the minimax algorithm

    Args:
        depth (int): The depth of the tree
        nodeIndex (int): The index of the node
        maximizingPlayer (bool): Whether the computer is the maximizing player
        values (list): The values of the nodes
        alpha (int): The alpha value
        beta (int): The beta value

    Returns:
        int: The best move for the computer
    """
    if depth == base_case:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta, base_case)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

    else:
        best = MAX

        # right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 +
                          i, True, values, alpha, beta, base_case)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best


# Driver Code

values = [5, 10, 11, 7, 8, 9, 0, 4, 3, 2, 1, 0, 9, 20, 25, 14]
base_case = math.ceil(math.log(len(values), 2))
print("The optimal value is :", minimax(
    0, 0, True, values, MIN, MAX, base_case))
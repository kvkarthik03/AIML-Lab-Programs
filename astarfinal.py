from queue import PriorityQueue

def calculate_heuristic(current_state,goal_state):
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != goal_state[i][j]:
                heuristic += 1
    return heuristic

def get_children(current_state,zero_row,zero_col):
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    children = []

    for move in moves:
        new_row,new_col = zero_row + move[0], zero_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = [row[:] for row in current_state]
            new_puzzle[new_row][new_col], new_puzzle[zero_row][zero_col] = 0,new_puzzle[new_row][new_col]
            children.append(new_puzzle)
    return children

def play_8_puzzle(initial_state,goal_state):
    open_set = PriorityQueue()
    closed_set = set()

    open_set.put((calculate_heuristic(initial_state,goal_state),initial_state))

    while not open_set.empty():
        current_heuristic,current_state = open_set.get()

        print_puzzle(current_state)
        print()

        if current_state == goal_state:
            print("\nGoal state reached!")
            print_puzzle(current_state)
            return
        
        closed_set.add(tuple(map(tuple,current_state)))
        zero_row,zero_col = find_zero_position(current_state)

        children = get_children(current_state,zero_row,zero_col)

        for child in children:
            if tuple(map(tuple,child)) not in closed_set:
                open_set.put((calculate_heuristic(child,goal_state),child))

def find_zero_position(current_state):
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == 0:
                return i,j

def print_puzzle(current_state):
    for row in current_state:
        for col in row:
            print(col,end=' ')
        print()

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 5], [8, 6, 7]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 
    play_8_puzzle(initial_state,goal_state)
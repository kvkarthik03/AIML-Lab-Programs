def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def is_winner(board,player):
    for row in board:
        count = 0
        for cell in row:
            if cell == player:
                count += 1
        if count == 3:
            return True
    
    for col in range(3):
        count = 0
        for row in board:
            if row[col] == player:
                count += 1
        if count == 3:
            return True
    
    if(board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i,j))
    return empty_cells

def minimax(board,depth,maximizingPlayer):
    if is_winner(board,'X'): return -1
    if is_winner(board,'O'): return 1
    if is_board_full(board): return 0

    best_eval = float('-inf') if maximizingPlayer else float('inf')

    for i,j in get_empty_cells(board):
        board[i][j] = 'O' if maximizingPlayer else 'X'
        eval = minimax(board,depth+1,not maximizingPlayer)
        board[i][j] = ' '

        if maximizingPlayer:
            best_eval = max(best_eval,eval)
        else:
            best_eval = min(best_eval,eval)
    return best_eval

def get_best_move(board):
    best_move,best_val = None,float('-inf')

    for i,j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board,0,False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move,best_val = (i,j),move_val
    return best_move

def play_tic_tac_toe():
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(' ')
        board.append(row)
    
    player_turn = True
    
    while True:
        print_board(board)

        if player_turn:
            row,col = map(int,input("Enter your move (row and col separated by space): ").split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Invalid move. Try again")
                continue
        
        else:
            print("Computer's move:")
            row,col = get_best_move(board)
            board[row][col] = 'O'

        if is_winner(board,'X'):
            print_board(board)
            print("User wins!")
            break

        elif is_winner(board,'O'):
            print_board(board)
            print("Computer wins!")
            break

        elif is_board_full(board):
            print_board(board)
            print("It's a tie")
            break

        player_turn = not player_turn
    
if __name__ == "__main__":
    play_tic_tac_toe()

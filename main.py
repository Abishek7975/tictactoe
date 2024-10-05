
def printBoard(board):
    symbols = {
        1: "X",
        -1: "O",
        0: " "
    }
    for i in range(3):
        row = []
        for j in range(3):
            row.append(symbols[board[i][j]])
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("---------")


def checkWinner(board):
    for row in board:  # Check rows
        if abs(sum(row)) == 3:
            return row[0]
    for col in range(3):  # Check columns
        if abs(sum([board[row][col] for row in range(3)])) == 3:
            return board[0][col]
    # Check diagonals
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]
    # Check for draw or no winner
    if all(cell != 0 for row in board for cell in row):
        return 0  # Draw
    return None  # Game ongoing

def minimax(board, depth, is_maximising):
    winner = checkWinner(board)
    if winner is not None:
        return winner

    if is_maximising:  # Player's turn (trying to maximize score)
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1  # Player places 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = 0  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:  # AI's turn (trying to minimize score)
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1  # AI places 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = 0  # Undo the move
                    best_score = min(score, best_score)
        return best_score
def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1  # AI places 'O'
                score = minimax(board, 0, False)  # Evaluate the move
                board[i][j] = 0  # Undo the move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move





def playGame():
    player = True
    while checkWinner(board) is None:
        if player:
            print("Player turn!")
            row, col = map(int, input("Enter the row and col seperated by space: ").split())
            if board[row][col] == 0:
                board[row][col] = 1
                player = False
            else:
                print('Invalid Input')
            printBoard(board)
        else:
            print("AI's move")
            move = best_move(board)
            print(move)
            if move:
                board[move[0]][move[1]] = -1
            printBoard(board)
            player = True

    winner = checkWinner(board)
    if winner == 1:
        print("Player Wins")
    elif winner == -1:
        print("AI Wins")
    else:
        print("Draw")


board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

playGame()


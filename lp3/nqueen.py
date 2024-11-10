# Define the size of the chessboard (N x N)
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()  # Add a newline for better readability between solutions

def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True

            # If placing queen doesn't lead to a solution, backtrack
            board[i][col] = 0  # Remove queen

    return False

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Call the function to solve the N-Queens problem
solveNQ()

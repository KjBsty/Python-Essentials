from random import shuffle

def check_board(board):
    for row in board:
        if check_list(row):
            return False
    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if check_list(col):
            return False
    return True

def check_list(lst):
    return any(lst[i]==lst[i+1] and lst[i]==lst[i+2] for i in range(len(lst)-2))

board = [[]]

while check_board(board):
    board = [1,2,3,4]*9
    shuffle(board)
    board = [board[i:i + 6] for i in range(0, len(board), 6)]

print(board)


[[3, 2, 4, 3, 3, 2],
 [1, 1, 2, 3, 1, 3],
 [1, 3, 3, 2, 2, 2],
 [4, 4, 1, 4, 1, 2],
 [1, 1, 4, 4, 2, 4],
 [2, 4, 4, 3, 3, 1]]

[[2, 3, 4, 1, 4, 1],
 [3, 4, 1, 1, 3, 4],
 [3, 1, 4, 1, 3, 4],
 [3, 4, 2, 4, 2, 1],
 [2, 1, 4, 2, 3, 2],
 [2, 2, 1, 3, 3, 2]]



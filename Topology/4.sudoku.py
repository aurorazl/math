
def isValid(board,x,y):
    for i in range(9):
        if i != x and board[i][y]==board[x][y]:     # 看该行是否有相同的数
            return False
    for j in range(9):
        if j != y and board[x][j]==board[x][y]:     # 看该列是否有相同的数
            return False
    for i in range(3*(x//3),3*(x//3+1)):
        for j in range(3*(y//3),3*(y//3+1)):        # 看该九宫内是否有相同的数
            if (i!= x or j!= y) and board[i][j]==board[x][y]:
                return False
    return True

def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for k in range(9):
                    board[i][j]= k+1
                    if isValid(board,i,j) and solveSudoku(board):   # 每次重新开始检查
                        return True
                    board[i][j]=0
                return False
    return True

def solveSudoku2(board,i,j):
    if i==8 and j==9:
        return True
    if j == 9:
        j = 0
        i=i+1
    while i<9:
        while j<9:
            if board[i][j]==0:
                for k in range(9):
                    board[i][j]= k+1
                    if isValid(board,i,j) and solveSudoku2(board,i,j+1):   # 每次重新开始检查
                        return True
                    board[i][j]=0
                return False

import numpy as np
board = np.full((9,9),0)
# solveSudoku2(board,0,0)
# solveSudoku(board)
print(board)

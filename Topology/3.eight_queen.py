import numpy as np

columns = None          # C[]列表的皇后已放置在哪些列，用个list来表示，for循环时遇到相应的j直接跳过
main_diag = None        # 占据的主对角线，list列表，i表示第i个斜对角线，避免了二维数组的麻烦，8*8的二维数组一共15个主对角线
anti_diag = None        # 负45°对角线，这里取到16个也不影响

def dfs(C,result,row):
    n = len(C)
    if row == n:
        solution = []           # 用于保存该次的皇后排列情况
        for i in range(n):
            s = ['-' for i in range(n)]
            for j in range(n):
                if j==C[i]:     # 对于所有排列没有攻击的情况，row==n走到了这一步，添加到result
                    s[j]='Q'
            solution.append(' '.join(s))
        result.append(solution)
        return

    for j in range(n):
        ok = columns[j]==0 and main_diag[row+j]==0 and anti_diag[row-j+n]==0
        if not ok:
            continue        # 表示攻击了
        C[row] = j
        columns[j] = main_diag[row+j]=anti_diag[row-j+n]=1
        dfs(C,result,row+1)
        C[row]=0     # 回溯，表示第row行的皇后，先放在j列后，再放回0，以便下次放在j+1列
        columns[j]=main_diag[row+j]=anti_diag[row-j+n]=0

def solveNQueens(n):
    global columns
    global main_diag
    global anti_diag
    columns = [0 for i in range(n)]
    main_diag = [0 for i in range(2*n)]
    anti_diag = [0 for i in range(2*n)]
    result = []
    C = [0 for i in range(n)]
    dfs(C,result,0)
    return result

for i in solveNQueens(8):
    for j in i:
        print(j)
    print('\n')


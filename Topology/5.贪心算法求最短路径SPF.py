import numpy as np

def SPF(cost,dist,n):
    for i in range(n):
        if cost[0,i]==-1:
            dist[i] = float('inf')  # 一开始初始化值时，v0到没有边的结点距离为-1，改为无穷大，表示到达不了
        else:
            dist[i]=cost[0,i]        # 初始化距离

    for i in range(1,n):        # 表示以第i个结点为中间结点，从v1经过中间结点Vi到Vj的最短距离
    # for i in [2,3,4,1,5,6]:
        for j in range(n):
            if cost[i,j]==-1:
                continue        # 结点反向的情况、正向但没有边的情况，取原来的最短距离
            dist[j]=min(dist[j],dist[i]+cost[i,j])
        print(dist)
    return dist

n = 7
dist = [-1 for j in range(n)]
cost = np.array([
    [0,20,50,30,-1,-1,-1],
    [-1,0,25,-1,-1,70,-1],
    [-1,-1,0,40,25,50,-1],
    [-1,-1,-1,0,55,-1,-1],
    [-1,-1,-1,-1,0,10,70],
    [-1,-1,-1,-1,-1,0,50],
    [-1,-1,-1,-1,-1,-1,0]
])

print(SPF(cost,dist,7))







import queue
import numpy as np
def topologic(indegree,gragh):
    n = len(indegree)
    toposort = []
    q = queue.Queue()
    for i in range(n):
        if indegree[i]==0:
            q.put(i)
    while not q.empty():
        cur = q.get()
        toposort.append(cur)
        for i in range(n):
            if gragh[cur,i]!=0:     # cur都是入度为0的结点，gragh只能是1，不可能是-1
                indegree[i] -= 1    # 删去该顶点时，删去从该顶点发出的全部有向边
                if indegree[i]==0:
                    q.put(i)
    return toposort
indegree = [1,1,0,1,2,2,2,1,0,1,1,1,2]
gragh = np.array([
    [0,1,-1,0,0,1,1,0,0,0,0,0,0],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,-1,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,-1,-1,0,0,0,0,0,0],
    [-1,0,0,-1,1,0,0,0,0,0,0,0,0],
    [-1,0,0,0,1,0,0,-1,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,-1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,-1,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,-1,0,0,0],
    [0,0,0,0,0,0,0,0,0,-1,0,0,1],
    [0,0,0,0,0,0,0,0,0,-1,0,-1,0]
])
print(topologic(indegree,gragh))
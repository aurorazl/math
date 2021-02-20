import numpy as np

def isPalindrome(s,start,end):
    while start<end and s[start]==s[end]:
        start += 1
        end -= 1
    return start >=end

def DFS(s,path,result,start):
    n = len(s)
    if start == n:
        result.append(path.copy())  # list的指针引用问题，直接赋值共用指针，copy新创建第一层指针，deepcopy创建所有指针
        return
    for i in range(start,n):
        if isPalindrome(s,start,i):
            path.append(s[start:i+1])
            DFS(s,path,result,i+1)
            path.pop()          # 因为深度优先搜索每一个深度到底后，都要回溯至分岔口，进行下一个分支的检索

def partition(s):
    result = []
    path = []
    DFS(s,path,result,0)
    return result

# print(partition('aaba'))

##################################动态规划法
def partition2(s):
    n = len(s)
    p = np.zeros((n,n))
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i]==s[j] and ((j-i)<2 or p[i+1,j-1]==1):       # 看是否回文串
                p[i,j]=1
            else:
                p[i,j] = 0
    sub_palins = [[] for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if p[i,j]:          # 如果是回文串
                palindrome = s[i:j+1]
                if j+1<n:
                    for v in sub_palins[j+1]:       # 表示子字符串的所有划分
                        # print(v)
                        tmp = v.copy()
                        tmp.insert(0,palindrome)
                        sub_palins[i].append(tmp)
                else:
                    sub_palins[i].append([palindrome])
    return sub_palins

# print(partition2('aab'))
###############################最小回文划分次数
def minCut(s):
    n = len(s)
    f = [0 for i in range(n+1)]
    p = np.zeros((n,n))
    for i in range(n+1):
        f[i]=n-1-i          # 最坏的情况：每个字符都切一下，n+1个值是因为j=n-1时与f[n]=-1+1=0比较
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i]==s[j] and ((j-i)<2 or p[i+1,j-1]==1):
                p[i,j]=1
                f[i]=min(f[i],f[j+1]+1) # 从不同的回文划分中选取最小值，每次不同的j都更新一下f[i]的值
    return f        # 返回的是切的刀数
print(minCut('aab'))

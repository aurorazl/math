# li=[1,2,3]
# lin=[i for i in range(len(li))]

def dfs(position,li):
    lin = [i for i in range(len(li))]
    if position==len(li):
        print(li)
        return
    for i in range(0,len(li)):
        if li[i]!=0:
            lin[position]=li[i]
            tmp=li[i]
            li[i]=0
            dfs(position+1,li)
            li[i]=tmp
# dfs([1,2,3])
# dfs(0)

def dfs1(li):
    for i in range(len(li)):
        if li[i]==0:
            continue
        print(li[i])        # 有时候不会全打印，从倒数第二个开始打印，因为递归
        tmp = li[i]
        li[i]=0
        dfs1(li)
        li[i]=tmp
        if i==len(li)-1:
            print("end")
# dfs1([1,2,3])

def permutations(li,start,end):
    if start==end:
        print(li)
    else:
        for i in range(start,end):
            li[start],li[i]=li[i],li[start]
            permutations(li,start+1,end)
            li[start], li[i] = li[i], li[start]
permutations([1,2,3],0,3)
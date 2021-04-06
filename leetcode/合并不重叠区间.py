
#
"""
思路：
维护一个列表，遍历输入列表，每个加入前先判断要加入的位置。
"""

def mergeLi(li):
    tmp = []
    for one in li:
        for t in tmp:
            if one[1]==t[0]-1:
                t[0] = one[0]
                break
            if one[0]==t[1]+1:
                t[1] = one[1]
                break
        else:
            tmp.append(one)
    return tmp

print(mergeLi([[1,10],[11,20],[40,45],[30,39]]))

def mergeLi2(li):
    sorted(li,key=lambda x:x[0])        # 用到内置排序方法
    tmp = []
    for i in range(0,len(li),2):
        if li[i+1][0]==li[i][1]+1:
            tmp.append([li[i][0],li[i+1][1]])
        else:
            tmp += li[i:i+1]
    return tmp
print(mergeLi2([[1,10],[11,20],[40,45],[30,39]]))
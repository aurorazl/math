"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

"""


# 深度递归
def splitArray(li):
    sum_li = sum(li)
    if sum_li%2!=0:
        return False
    target = sum_li/2
    return findvalue(li, target)

def findvalue(li,target):
    if target==0:
        return True
    if li and target<li[0]:
        return False
    for i in li:
        if findvalue(li[1:],target-i):
            return True
    return False

# print(splitArray([1,5,11,5]))

import copy
def func(li):
    sum_li = sum(li)
    if sum_li%2!=0:
        return False
    k = sum_li// 2
    tmp = {i: 0 for i in range(0, k + 1)}
    use = {i: [] for i in range(0, k + 1)}
    tmp[0]=1
    for index,i in enumerate(li):
        for j in range(i,k+1):
            print(i,j,use,tmp)
            if j==i:
                tmp[j] += tmp[j-i]
                use[j].append([index])
            else:
                for one in use[j-i]:
                    if index not in one and one:
                        tmp[j] += 1
                        one_tmp = copy.copy(one)
                        one_tmp.append(index)
                        use[j].append(one_tmp)
                if j==k and tmp[j]!=0:
                    return True

    return False

print(func([5,5,4,4,3,1]))

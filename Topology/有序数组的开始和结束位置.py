#coding=utf-8
"""
二分查找Ⅱ-查找指定元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
"""

def findValueIndex(li,target):
    if len(li)<1:
        return [-1,-1]
    i = j = 0
    while i<len(li):
        if li[i]!=target:
            i += 1
            continue
        if li[i]==target:
            break
        if li[i]>target:
            i=-1
            break
    j = i
    if i==-1:
        return [-1,-1]
    while j <len(li):
        if li[j]>target:
            break
        j+=1
    return [i,j-1]

# print(findValueIndex([],7))
# 思路：找左右指标，分开二分找即可。


def binarySearchIndex(li,target):
    if len(li)<1:
        return [-1,-1]

    def binarySearch(li,target,lower):
        i = 0
        j = len(li)-1
        ans = len(li)
        while i<=j:
            mid = (i+j)//2
            if li[mid]>target or (lower and li[mid]>=target):
                j = mid-1
                ans = mid
            else:
                i = mid + 1
        return ans

    left = binarySearch(li,target,True)
    right = binarySearch(li,target,False)-1
    if left<=right and right<len(li) and li[left]==target and li[right]==target:
        return [left,right]
    return [-1,-1]
print(binarySearchIndex([1],1))




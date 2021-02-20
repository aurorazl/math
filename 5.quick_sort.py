import time_calculate
import sys
import random
sys.setrecursionlimit(1000000000)
def _quick_sort(li,left,right):  # left：列表的第一个元素下表，right：最后一个元素下标
    if left < right:
        mid = partition(li,left,right)  # 返回列表的第一个元素归为位置
        _quick_sort(li,left,mid-1)
        _quick_sort(li,mid+1,right)

@time_calculate.cal_time        # 装饰器就是把一个函数替换了，如果递归函数的话会多次装饰，解决：套一个马甲，函数内执行递归函数即可
def quick_sort(li):
    _quick_sort(li,0,len(li)-1)

def partition(li,left,right):
    i = random.randint(left,right)
    li[left],li[i]=li[i],li[left]
    tmp = li[left]
    while left < right:
        while left<right and li[right]>=tmp:    # 从右边找比tmp小的数
            right -= 1
        li[left]=li[right]          # 找到比tmp小的数，它取代tmp位置，即left位置，且tmp位置默认放到了right位置，因为与tmp比较大小
        # left += 1
        while left < right and li[left]<= tmp:  # 从左边找比tmp大的数
            left += 1
        li[right] = li[left]
        # right -= 1    # 不能+1是因为下一步还要赋值li[left] = tmp
    li[left] = tmp  # 最后left或right赋值tmp
    return left

@time_calculate.cal_time
def sys_sort(li):
    li.sort()

import copy
# li = list(range(10000))
li3 = list(range(100000,0,-1))    # 倒序
# li2 = copy.deepcopy(li)
# random.shuffle(li)      # 随机排序
quick_sort(li3)
# sys_sort(li2)
print(li3)
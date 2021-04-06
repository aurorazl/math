from sort import time_calculate


def sift(li,low,high):
    tmp = li[low]
    i=low
    j=2*i+1
    while j<=high:
        if j<high and li[j+1]>li[j]:    # j<high：存在右孩子，如果=那么j+1大于hight
            j+=1        # 不必考虑tmp放左还是放右，都一样满足最大堆的定义，这里是先放右，再放左
        if tmp < li[j]:    # 跟节点和左右中最大的比较
            li[i]=li[j]
            i=j
            j=2*i+1
        else:
            break       # 第一种跳出条件：根节点大于孩子节点
    li[i]=tmp       # 第二种条件：是叶子节点了

# li = [2,9,7,8,5,0,1,6,4,3]
# sift(li,0,len(li)-1)
# print(li)

@time_calculate.cal_time
def heap_sort(li):
    n = len(li)
    # 1.建堆
    for i in range(n//2-1,-1,-1):   # 如果最后的叶子节点下标是n-1，那么最后一个非叶子节点是(n-1-1)//2,
        sift(li,i,n-1)      # 不断调整各个子树为最大堆，传根节点和最大值，这里统一n-1能适用所有子树，而不用求子树对应的最右边叶子节点  # 顺序：从末支开始调整，和取值的顺序相反。
    # print(li)
    # 2.挨个出数
    for i in range(n-1,-1,-1):  # i表示此时堆的high位置,high：属于堆的范围
        li[0],li[i]=li[i],li[0]     #退休棋子和上任棋子交换
        sift(li,0,i-1)          # 退休不再属于堆
    # 3.再回到循环
# li = [6,8,1,9,3,0,7,2,4,5]
# heap_sort(li)
import random
li = list(range(100000))
random.shuffle(li)      # 随机排序
heap_sort(li)
print(li)
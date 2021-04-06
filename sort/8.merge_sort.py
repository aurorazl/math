
def merge(li,low,mid,high):
    i = low
    j = mid+1
    li_tmp = []
    while i<=mid and j <=high:
        if li[i]<li[j]:            #
            li_tmp.append(li[i])
            i+=1
        else:
            li_tmp.append(li[j])
            j += 1
    while i<=mid:           # 上一个循环结束后，会有一边还没取完，下面两个循环会有一个执行
        li_tmp.append(li[i])
        i += 1
    while j<=high:
        li_tmp.append(li[i])
        j += 1
    # li[low:high+1]=li_tmp         # 另一种方法
    for i in range(low,high+1):
        li[i]=li_tmp[i-low]     # li整个列表可能就两段有序的,i-low表示0开始，high+1-low结尾

li=[2,5,7,8,9,1,3,4,6]
merge(li,0,4,8)         # 这就实现了一次归并
print(li)

def merge_sort(li,low,high):
    if low<high:        # 至少两个元素
        mid = (low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

import random
li = list(range(100))
random.shuffle(li)      # 随机排序
merge_sort(li,0,99)
print(li)
def bubble(li):
    n = len(li)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]   # 在不断缩小的范围内将最大值放到最后
    return li

def select(li):
    for i in range(0,len(li)):
        min = i
        for j in range(i+1,len(li)):
            if li[j]<li[min]:
                min = j
        li[i], li[min] = li[min], li[i] # 在不断缩小的范围内选出最小值放到前面

def insert1(li):
    for i in range(1,len(li)):
        tmp = li[i]
        for j in range(i-1,-1,-1):
            if li[j]>tmp:
                li[j], li[j + 1] = li[j + 1], li[j] # 将前后值比较，如果后面值小就放到前面
            else:
                break
    return li

def insert2(li):
    for i in range(1,len(li)):
        tmp = li[i]
        for j in range(i-1,-1,-1):
            # print(i,j)
            if li[j]>tmp:
                li[j + 1] = li[j]
                if j == 0:
                    li[j] = tmp # 两种终止条件需要将tmp值补上，情况一：j==0即将退出循环
            else:
                li[j+1] = tmp   # 情况二：前面值小，即将退出循环，可以用while循环更方便
                break
    return li

def search(li,a):
    start = 0
    end = len(li)-1
    while start <= end:
        mid = (start+end)//2
        if li[mid]>a:
            end = mid -1
        elif li[mid]<a:
            start = mid +1
        else:
            return mid
    else:
        return None

def quick(li):
    def _quick(li,start,end):
        if start <end:
            mid = partion(li,start,end)
            _quick(li,start,mid-1)
            _quick(li,mid+1,end)

    def partion(li,start,end):
        import random
        i = random.randint(start,end)
        li[start],li[i] = li[i],li[start]
        tmp = li[start]
        while start< end:
            while li[end]>=tmp and start<end:   # 两个指针在不停的移动
                end -=1
            li[start]=li[end]
            while li[start]<=tmp and start<end:
                start +=1
            li[end]=li[start]
        li[start] = tmp     # start = end 时不用比较了，这个即tmp的位置
        return start

    return _quick(li,0,len(li)-1)

def sift(li,low,high):
    left = low * 2 + 1
    right = low * 2 + 2
    tmp = li[low]
    while left<=high:
        if right <= high and li[left]<li[right]:        # 右节点存在且右节点大，比较右节点
            left+=1
        if li[left]>tmp:
            li[low] = li[left]          #　如果大，则将节点赋值到跟节点
            low = left
            left = low * 2 + 1
            right = low * 2 + 2
        else:
            break
    li[low] = tmp

def heap(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1): # 从最下开始建堆
        sift(li,i,n-1)
    for i in range(n-1,0,-1):
        li[0],li[i] = li[i],li[0]   # 取数
        sift(li,0,i-1)

def merge(li,low,mid,high):
    tmp = []
    i = low
    j = mid +1
    while i<=mid and j <=high:
        if li[i]<li[j]:
            tmp.append(li[i])
            i += 1
        elif li[j]<=li[i]:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low:high+1] = tmp    #　错误点１:一开始直接使用low和high作为移标移动，这步就会出错
    return li

def merge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li, low, mid, high)


import random
li = list(range(1000))
# print(search(li,2.5))
random.shuffle(li)
print(li)
# bubble(li)
# select(li)
# insert2(li)
# quick(li)
# heap(li)
merge_sort(li,0,len(li)-1)
print(li)




import random,time
from time_calculate import cal_time,cal_time_foo

def _quick_sort(li,left,right):
    if left<right:
        mid = partition(li,left,right)
        _quick_sort(li,left,mid-1)
        _quick_sort(li,mid+1,right)

@cal_time
def quick_sort(li):
    _quick_sort(li,0,len(li)-1)

def partition(li,left,right):
    i = random.randint(left,right)
    li[left], li[i] = li[i], li[left]
    temp = li[left]
    while left < right :
        while left<right and li[right]>=temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <=temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left

def sift(li,low,high):
    temp = li[low]
    i = low
    j = low*2+1
    while j<=high:
        if j<high and li[j+1]>li[j]:
            j+=1
        if temp <li[j]:
            li[i] = li[j]
            i = j
            j = 2*i +1
        else:
            break
    li[i]=temp

@cal_time
def heap(li):
    n = len(li)
    for i in range(n//2-1,-1,-1):
        sift(li,i,n-1)
    for j in range(n-1,-1,-1):
        li[j],li[0]=li[0],li[j]
        sift(li,0,j-1)


def merge(li,low,mid,high):
    i = low
    j = mid+1
    tmp = []
    while i<=mid and j<=high:
        if li[i]<li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i<=mid:
        tmp.append(li[i])
        i+=1
    while j<=high:
        tmp.append(li[j])
        j+=1
    for i in range(low,high+1):
        li[i] = tmp[i-low]

def _merge_sort(li,low,high):
    if low<high:        # 至少两个元素
        mid = (low+high)//2
        _merge_sort(li,low,mid)
        _merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

@cal_time
def merge_sort(li):
    _merge_sort(li,0,len(li)-1)
    # print('done')

@cal_time
def test(li):
    print('done')

# print(test.__name__)
# test = cal_time_foo(test)
# test('czl')

if __name__=='__main__':
    for j in range(6,9):        # 测试完成，区别不大
        print("开始测试10的%s次方长度的列表排序"%j)
        li = list(range(10**j))
        random.shuffle(li)
        # print(li)
        import threading
        import multiprocessing
        fun_list = [quick_sort,heap,merge_sort]
        for i in fun_list:
            i(li)
            # p = multiprocessing.Process(target=i,args=(li,))  # 装饰器通过wrap解决pickle问题
            # p = threading.Thread(target=i,args=(li,))
            # p.start()



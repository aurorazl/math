# 利用快排，或者堆排，维护最大堆
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

def find_top_k(data_list,K):
    length = len(data_list)
    begin = 0
    end = length-1
    index = partition(data_list,begin,end) #这里的partition函数就是上面快排用到的函数
    while index != length - K:
        if index >length - K:
            index = partition(data_list,begin,index)
        else:
            index = partition(data_list,index+1,end)
    return data_list[index]

li = list(range(10000))
import random
random.shuffle(li)
print(f"第 {1} 大元素是 {find_top_k(li,3)}")
import time_calculate
@time_calculate.cal_time
def bubble_sort(li):
    for i in range(0,len(li)-1):    # len(li)的话j取不到，即（0，-1）
        flag = True
        for j in range(0,len(li)-i-1):
            print(i,j)
            if li[j]>li[j+1]:
                flag = False
                li[j],li[j+1] = li[j+1],li[j]
        if flag:
            return      # 优化：如果经过一轮，而没有交换，则列表已是有序状态

import random
# li = list(range(10))
# random.shuffle(li)      # 随机排序
li=[1,3,2]
bubble_sort(li)
print(li)
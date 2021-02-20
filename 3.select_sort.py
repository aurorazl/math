import time_calculate

@time_calculate.cal_time
def select_sort(li):
    for i in range(0,len(li)-1):
        # 第i趟：有序区li[0,i] 无序区li[i,n]
        min_loc = i
        for j in range(i+1,len(li)):    #每次确定一个最小数，从头到尾确定
            if li[min_loc]>li[j]:       #从已确定数后一位开始
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]

import random
li = list(range(10000))
random.shuffle(li)      # 随机排序
select_sort(li)
# print(li)
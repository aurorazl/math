from sort import time_calculate


@time_calculate.cal_time
def insert_sort(li):
    for i in range(1,len(li)):
        # i表示第几趟，也表示摸到的牌的下表，默认第一个牌li[0]是有序区
        j = i-1
        tmp = li[i]
        while j>=0 and li[j]>tmp:   # 布尔语句短路 a and b：a真不判断b   a or b ：a假不判断b
            li[j+1] = li[j]
            j -=1
        li[j+1] = tmp       # 该趟摸到的牌插到比他小之后

import random
li = list(range(10000))
random.shuffle(li)      # 随机排序
insert_sort(li)
# print(li)
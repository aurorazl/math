import heapq

import random
li = list(range(100000))
random.shuffle(li)

heapq.heapify(li)
# print(li)
print(heapq.heappop(li))    # 取出退休的，内部会重新调整

def heap_sort(li):
    h=[]
    for value in li:
        heapq.heappush(h,value)
    return [heapq.heappop(h) for i in range(len(h))]
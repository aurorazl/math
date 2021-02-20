import time
def cal_time(func):
    def warpper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time:%s"%(func.__name__,t2-t1))
    return warpper


@cal_time
def search(li, val):
    low = 0
    high = len(li)-1
    count = 0
    while low <= high:
        count +=1
        mid = (low + high) // 2
        # print("mid",mid,li[mid])
        if li[mid] > val:
            high = mid - 1
            # print("high",high)
        elif li[mid] < val:
            low = mid + 1
            # print("low",low)
        else:
            print(count)
            return mid
    else:
        print(count)
        return None
@cal_time
def linner_search(li,val):
    try:
        i = li.index(val)
        return i
    except Exception as e:
        return 0
import random
li = list(range(1,1000000))
val = random.choice(li)

search(li,val)
linner_search(li,val)

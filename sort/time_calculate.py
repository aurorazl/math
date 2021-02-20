import time
import functools

def cal_time(func):
    @functools.wraps(func)
    def warpper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time:%s"%(func.__name__,t2-t1))
    return warpper

class cal_time_foo(object):

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.func(*args,**kwargs)
        t2 = time.time()
        print("%s running time:%s"%(self.func.__name__,t2-t1))
        return result
import threading
class Singleton(object):

    _instance_lock = threading.RLock()
    def __init__(self):
        # pass
        import time
        time.sleep(1)           # 不加锁时，会出现一开始创建_instance属性时阻塞，导致下一个线程检测到还没有_instance属性

    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance



def task(arg):
    obj = Singleton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()



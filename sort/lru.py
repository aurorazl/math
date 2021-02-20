

class _lru_cache_wrapper():
    sentinel = object()  # unique object used to signal cache misses
    PREV, NEXT, KEY, RESULT = 0, 1, 2, 3  # names for the link fields
    maxsize=5
    cache = {}
    hits = misses = 0
    full = False
    cache_get = cache.get  # bound method to lookup a key or return None
    cache_len = cache.__len__  # get cache size without calling len()
    root = []  # root of the circular doubly linked list
    root[:] = [root, root, None, None]

    def get(self,key):
        link = self.cache_get(key)
        if link is not None:
            link_prev, link_next, _key, result = link
            link_prev[self.NEXT] = link_next
            link_next[self.PREV] = link_prev
            last = self.root[self.PREV]
            last[self.NEXT] = self.root[self.PREV] = link
            link[self.PREV] = last
            link[self.NEXT] = self.root
            self.hits += 1
            return result

    def set(self,key,result):
        if key in self.cache:
            pass
        elif self.full:
            oldroot = self.root
            oldroot[self.KEY] = key
            oldroot[self.RESULT] = result
            root = oldroot[self.NEXT]
            oldkey = root[self.KEY]
            self.oldresult = root[self.RESULT]
            root[self.KEY] = root[self.RESULT] = None
            del self.cache[oldkey]
            self.cache[key] = oldroot
        else:
            last = self.root[self.PREV]
            link = [last, self.root, key, result]
            last[self.NEXT] = self.root[self.PREV] = self.cache[key] = link
            self.full = (self.cache_len() >= self.maxsize)

a = _lru_cache_wrapper()
a.set("a",1)

def package_max_value(li,cap):
    max_value=[0 for i in range(cap)]
    in_package = set()
    for i in range(cap):
        for j in li:
            # 目标：求当前容量下能装下的物品最大价值
            if j.weight<i+1 and j.name not in in_package:		# 小于当前容量，说明容量有剩，那么比较剩余容量的最大价值+当前物品的价值 vs 当前容量的最大价值
                if j.value+max_value[i-j.weight]>max_value[i]:
                    max_value[i] = j.value+max_value[i-j.weight]
                    in_package.add(j.name)
            elif j.weight==i+1:	# 刚好没有容量剩余，那么比较当前物品的价值的价值即可
                if j.value>max_value[i]:
                    max_value[i] = j.value
                    in_package.clear()
                    in_package.add(j.name)
            # 容量不够，那么不考虑当前物品
    return max_value[-1]

from collections import namedtuple
thing = namedtuple("thing",'name weight value')
li = [thing("phone",1,1500),thing("gita",3,2000),thing("ganqin",4,3000)]
print(package_max_value(li,5))
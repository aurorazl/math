
def package_max_value(li,cap):#错误，物品集合没有更新的操作
    max_value=[0 for i in range(cap)]
    in_package = set()
    for i in range(cap):        # 当容量为1，2，3，4，5.。。。。时
        for j in li:        # 遍历物品
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

def package_max_value2(li,cap):
    dp=[[0 for _ in range(cap+1)] for _ in range(len(li)+1)]
    for i in range(1,len(li)+1):        # 遍历物品
        for j in range(1,cap+1):  # 当容量为1，2，3，4，5.。。。。时
            if li[i-1].weight<=j :		# 容量能放得下
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-li[i-1].weight]+li[i-1].value) #是否要当前物品，dp[i-1]排除了重复使用物品的可能性
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

def package_max_value3(li,cap):
    dp=[0 for _ in range(cap+1)]
    for i in range(1,len(li)+1):        # 遍历物品
        for j in range(cap,li[i-1].weight-1,-1):  # 当容量为1，2，3，4，5.。。。。时
            dp[j] = max(dp[j],dp[j-li[i-1].weight]+li[i-1].value) #倒序，防止高位用了该物品，低位再次用到该物品。因为高位先用
    return dp[-1]

from collections import namedtuple
thing = namedtuple("thing",'name weight value')
li = [thing("phone",1,1500),thing("gita",3,2000),thing("ganqin",4,3000)]
print(package_max_value3(li,5))

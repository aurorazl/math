
def change_max_cnts(changes,k): # 该方法目前错误，待改进,需要忽略重复的，而且累加方式不同，总的来说，这个角度不好
    cnts = [0 for _ in range(k)]
    for i in range(k):              # 对于每个价格，寻找各个面值组成的最大换算次数
        for j in changes:           #
            if j==i+1:
                cnts[i]+=1
            elif j<i+1 and i+1-j>=j:    # 由于3=1+2=2+1，而2由1换算而来，忽略掉那些
                cnts[i] += cnts[i-j]
    return cnts[-1]

def change_max_cnts2(changes,k):
    cnts = [0 for _ in range(k+1)]
    cnts[0]=1
    for change in changes:               # 对于每种面值，寻找 0 - 最大价格 范围内的价格的组合，因为最大价格可分解为较小价格+一种面值，将问题分解为不同面值下每种价格的换法
        for i in range(k-change+1):      # 从0到最大值-当前零钱，0表示本身面值有一种换法，以1为间隔，而不是change为间隔，这样肯定不会漏掉某个价格的次数更新，以最小面值也不行
            cnts[change+i]+=cnts[i]       # 表示换成该零钱，可由cnts[i]价格加该面值换来
    print(cnts[1:])
    return cnts[k]

print(change_max_cnts2([1,2],6))

# 和为定值的多个零钱组合的次数，零钱可以重复取
def func2(coins,amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):      # 优化，直接跳过小面值
            dp[x] += dp[x - coin]               # coin是2的时候，无法使用coin为3的情况，避免了2+3的情况，只能3+2
    return dp[amount]

import copy
def func22(coins,amount):
    dp = [0] * (amount + 1)
    m = [[]] * (amount + 1)
    dp[0] = 1
    def is_valid(x,coin,y):
        for u in x:
            u.append(coin)
            for i in y:
                if u.issubset(i):       # TODO,需要判断两个列表是否相同，条件不好写
                    return False
        return True
    for x in range(1, amount + 1):  # 优化，直接跳过小面值
        for coin in coins:
            if x>=coin and is_valid(copy.deepcopy(m[x-coin]),coin,copy.deepcopy(m[x])):
                dp[x] += dp[x - coin]     # 有可能大的零钱重复出现过
                if x==coin:
                    m[x]=[[coin]]
                else:
                    for y in m[x-coin]:
                        y.add(coin)
                        m[x].append(y)
    print(m)
    return dp[amount]

print("func2",func2([1,2,5],5))
# print("func22",func22([1,2,5],5))

# 扩展： 和为定值的最少零钱个数
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 解决：
def func3(coins,amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):      # 优化，直接跳过小面值
            dp[x] =  min(dp[x], dp[x - coin] + 1)
    return dp[amount]

print(11,func3([3,2],8))

def func4(coins,amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for x in range(1,amount + 1):  # 优化，直接跳过小面值
        for coin in coins:
            if x-coin>=0:
                dp[x] =  min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount]!=float('inf') else -1
print(func4([1,2,5],5))
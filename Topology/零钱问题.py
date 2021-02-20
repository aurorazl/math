
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
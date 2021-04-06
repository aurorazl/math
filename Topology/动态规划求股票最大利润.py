
def one_buy_sell(li):
    high = 1
    low = 0
    result = max(li[high]-li[low],0)   # 最多一次买卖，如果一直亏，就一直不入手。
    for i in range(2,len(li)):
        if li[i]<li[low]:       # 目前最低价格
            low=i
        if li[i]-li[low] > result:  # 当前买卖大于历史收益
            result = li[i]-li[low]      # 兼容【7，3，7，1，3】
    return result

print(one_buy_sell([3,2]))

def mutli_buy_sell(li):
    sum_p = 0
    low = 0
    for i in range(1,len(li)):
        if li[i]<li[i-1]:                   # 处于下降趋势，昨天就卖出，说明昨天是最高点
            sum_p += li[i-1] - li[low]      # 如果一直下降，则一直没买卖，i-1==m
            low=i
        else:
            if i==len(li)-1:                # 上升阶段，什么都不做，除了到了最后一天了（肯定区间的最高点了），就卖出
                sum_p += li[i] - li[low]
    return sum_p

def two_buy_sell(li,k=2):                        # 动态规划思想：k次买卖，那么对于每一天，都有第k次买入或卖出的可能，买入条件为剩的钱最多，卖出条件为这次买卖获得利润最大
    buy = [float("-inf") for _ in range(k)]     # 初始状态为负无穷，那么一定会买入
    sell = [0 for _ in range(k)]                # 至少最大利润为0，总不能亏钱，如果买卖小于0就不进行
    for i in li:
        for j in range(0,k):        # 第k次的买卖，依赖于k-1的最优解
            # sell[j+1] = max(sell[j+1],buy[j+1]+i)
            # buy[j+1] = max(buy[j+1],sell[j]-i)
            sell[j] = max(sell[j],buy[j]+i)         # 如果buy[0]+i一直小于0，buy[0]买入就不算，最终的sell最大为0
            buy[j] = max(buy[j],sell[j-1]-i) if j>0 else  max(buy[j],-i)                 # -i表示买入后，用的钱最少，剩的钱最多
            print(i,j,buy,sell)
    return sell[k-1]

def two_buy_sell2(li,k=2):
    buy = [float("-inf") for _ in range(k)]
    sell = [0 for _ in range(k)]
    max_buy_day = [0 for _ in range(k)]
    max_sell_day = [0 for _ in range(k)]
    for j in range(0, k):
        for index,i in enumerate(li):
            if sell[j] < buy[j]+i and i not in max_sell_day:     # 记录一下买入卖出的天数
                sell[j]=buy[j]+i
                max_sell_day[j] = i
            if j>0 and buy[j]<sell[j-1]-i and i not in max_buy_day:
                buy[j] = sell[j-1]-i
                max_buy_day[j] = i
            if j<= 0 and buy[j]< -i and i not in max_buy_day:
                buy[j] = -i
                max_buy_day[j] = i
            print(i,j,buy,sell)
    return sell[k-1]

# 新的理解： 今天的结果依赖于昨天的买卖最优解，最外层循环是天数，里层是k。第一次的买入依赖第0次的卖出减去价格。k次交易顺序可以换。（因为昨天的结果是最优的，钱最多，今天到结束的这段时间内第k次要买入的话，必须价格最低）
# 简单来说，每天都算一下买入卖出是否最大值

print(two_buy_sell2([2,3,-5,4,3,2]))
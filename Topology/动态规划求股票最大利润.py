
def one_buy_sell(li):
    high = 1
    low = 0
    result = li[high]-li[low]
    for i in range(2,len(li)):
        if li[i]<li[low]:
            low=i
        if li[i]-li[low] > result:
            result = li[i]-li[low]
    return result

def mutli_buy_sell(li):
    sum_p = 0
    low = 0
    for i in range(1,len(li)):
        if li[i]<li[i-1]:
            sum_p += li[i-1] - li[low]
            low=i
        else:
            if i==len(li)-1:
                sum_p += li[i] - li[low]
    return sum_p

def two_buy_sell(li,k=2):                        # 动态规划思想：k次买卖，那么对于每一天，都有第k次买入或卖出的可能，买入条件为剩的钱最多，卖出条件为这次买卖获得利润最大
    buy = [float("-inf") for _ in range(k)]     # 初始状态为负无穷，那么一定会买入
    sell = [0 for _ in range(k)]                # 至少最大利润为0，总不能亏钱，如果买卖小于0就不进行
    for i in li:
        for j in range(0,k):
            # sell[j+1] = max(sell[j+1],buy[j+1]+i)
            # buy[j+1] = max(buy[j+1],sell[j]-i)
            sell[j] = max(sell[j],buy[j]+i)         # 如果buy[0]+i一直小于0，buy[0]买入就不算，最终的sell最大为0
            buy[j] = max(buy[j],sell[j-1]-i) if j>0 else  max(buy[j],-i)                 # -i表示买入后，用的钱最少，剩的钱最多
    return sell[k-1]

print(two_buy_sell([2,3,-5,4,3,2]))
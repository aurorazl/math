# 给定一组数，求能组合的和为指定数的所有组合


def func(changes,k):
    tmp = {i:0 for i in range(1,k+1)}
    for i in changes:
        key = sorted(list(tmp.keys()),reverse=True)
        for j in key:
            if not j+i in key:
                tmp[j + i] = 0
            tmp[j+i] += tmp[j]
        if i not in key:
            tmp[i]=1
        else:
            tmp[i] += 1
    print(tmp)
    return tmp[k] if k in tmp else None

print(func([2,3,5],5))

def func(changes,k):
    tmp = {i: 0 for i in range(0, k + 1)}
    use = {i: [] for i in range(0, k + 1)}
    tmp[0]=1
    for i in changes:
        for j in range(i,k+1):                                      # 限制：数字在该轮k遍历的时候出现过一次，只要确保k变化的时候，数字只用到一次即可，比如2、4只能用一次2
            if i not in use[j-i] and (j==i or (j>i and use[j-i])):  #
                tmp[j] += tmp[j-i]
                use[j].append(i)
                use[j]+=use[j-i]
    return tmp[k]
print(func([2,3,5],5))

def func2(changes,k):
    tmp = {i: [] for i in range(0, k + 1)}
    for j in range(1, k + 1):               #
        for i in changes:
            if j>=i and i not in tmp[j-i] and (j==i or (j>i and tmp[j-i])) and i not in tmp[j]:  # 然后就是组合，条件是tmp[j-i]和tmp[j]没有使用过
                tmp[j] += tmp[j-i]
                tmp[j].append(i)
    return tmp[k]
print(func2([2,3,5],8))

# 扩展：寻找和为定值的两个数
"""
方法1： hash，遍历
"""
class Solution:
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # python中字典dict类似于map的
        dict = {}
        for i in range(len(num)):   #  对于每一个num
            # 判断target - num[i]在不在在字典中
            if dict.get(target - num[i], None) == None: #如果不在
                dict[num[i]] = i   # 将该数存入字典中
            else:
                # 否则这两个数的和为target, 则返回
                return (dict[target - num[i]] , i )

### 方法2： 排序后双指针


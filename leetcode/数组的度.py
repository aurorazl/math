"""
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：

输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2：

输入：[1,2,2,3,1,4,2]
输出：6
 
提示：
nums.length 在1到 50,000 区间范围内。
nums[i] 是一个在 0 到 49,999 范围内的整数。
"""

def getDuOfList(li):
    cnt = {}
    for i in li:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    max_Du = max(cnt.values())
    return max_Du

def getSameDuOfList(li):
    max_Du = getDuOfList(li)
    for i in range(len(li)):
        for j in range(len(li)):
            tmp = li[j:j+i+1]       # 列表每个元素+下一个元素组成列表，看看是否满足，进而下二个元素。
            tmp_Du = getDuOfList(tmp)
            if max_Du==tmp_Du:
                return i+1

li = [1,2,2,3,1]
print(getSameDuOfList(li))

### 上述解法相当于广度遍历，把所有的可能遍历一次，从最小长度开始，遇到适合的情况便可以提前退出,时间复杂度为O(t*t)

### 优化：最短列表肯定包含了度的元素x，并且x可能多个。只要记录x出现的首位、尾位即可。时间复杂度为O(1)

def getShortestLenEqualDuOfList(li):
    cnt = {}
    for index,i in enumerate(li):
        if i not in cnt:
            cnt[i] = [index,index,1]
        else:
            cnt[i][1] = index
            cnt[i][2] += 1
    Du = 0
    length = 0
    for k,v in cnt.items():
        if v[2]>Du:
            Du = v[2]
            length = v[1]-v[0]
        else:
            if v[2]==Du and v[1]-v[0]<length:
                length = v[1] - v[0]
    return length+1

print(getShortestLenEqualDuOfList(li))




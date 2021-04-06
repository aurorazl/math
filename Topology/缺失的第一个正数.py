

### 方法
"""
1.遍历hash存储，然后遍历看哪个数不存在
2.置换法，遍历
对数组进行一次遍历，对于遍历到的数 x = \textit{nums}[i]x=nums[i]，如果 x \in [1, N]x∈[1,N]，我们就知道 xx 应当出现在数组中的 x - 1x−1 的位置，
因此交换 \textit{nums}[i]nums[i] 和 \textit{nums}[x - 1]nums[x−1]，这样 xx 就出现在了正确的位置。在完成交换后，新的 \textit{nums}[i]nums[i] 可能还在 [1, N][1,N] 的范围内，
我们需要继续进行交换操作，直到 x \notin [1, N]x∈
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:                   # nums[nums[i] - 1] == nums[i] 表示i所在的位置已经对上了nums[i] - 1，可以退出
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]                 # 1 <= nums[i] <= n可以避开【1，5，3，4】这种情况，直接到3
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

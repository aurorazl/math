"""
每次向内移动短板，所有的消去状态都不会导致丢失面积最大值 。
"""

class Solution:
    def maxArea(self, height) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


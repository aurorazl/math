"""
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1]
, ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
"""

def search(nums, target) -> int:
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


def searchValue(li,value):
    return searchValueRange(li,0,len(li)-1,value)

def searchValueRange(li,left,right,value):
    if right< left:
        return -1
    mid = (left+right)/2
    if li[mid]==value:
        return mid
    if li[mid]<li[right]:
        if value> li[mid] and value<li[right]:
            return searchValueRange(li,mid+1,right,value)
        else:
            return searchValueRange(li,left,mid-1,value)
    else:
        if value< li[mid] and value> li[left]:
            return searchValueRange(li,left,mid,value)
        else:
            return searchValueRange(li,mid+1,right,value)


"""
扩展，找旋转后的最小值
"""

class Solution:
    def findMin(self, nums) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]

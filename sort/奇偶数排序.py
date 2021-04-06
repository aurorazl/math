"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

# 简单排序，遍历一次，放奇数和偶数分开存放，最后合并，时间复杂度O(n)，空间复杂度O(n)


# 要求空间复杂度为O(1)
# 那就要直接在原列表上操作，双指针法
#
# 左指针从头开始找偶数，右指针从尾开始找奇数，然后交换位置。
def exchange(li):
    left,right = 0,len(li)-1
    while left<right:
        if li[left]%2==1:
            left += 1
            continue
        if li[right]%2==0:
            right-=1
            continue
        li[left],li[right] = li[right],li[left]
    return li
print(exchange([1,2,3]))

# 快慢双指针

def exchange2(li):
    low,fast = 0,0
    while fast<len(li):
        if li[fast]%2==1:
            li[low], li[fast] = li[fast], li[low]
            low+=1                  # low的作用是存放fast找到的奇数，fast从第一位开始找，不会漏掉开头
        fast+=1
    return li

print(exchange2([2,4,1,3]))

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""
class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next=next

def addTwoNumbers(p,q):
    carry=0
    curr = Node()
    c = curr
    while p or q:
        x,y = 0,0
        if p:
            x = p.val
            p = p.next
        if q:
            y = q.val
            q = q.next
        sum_x_y = carry+x+y     # 求和，包含进位
        carry = sum_x_y//10     # 进位
        sum_x_y = sum_x_y%10   # 余数
        curr.val = sum_x_y
        curr.next = Node()
        curr = curr.next
    return c

a = Node(2,Node(4,Node(3)))
b = Node(9,Node(6,Node(4,Node(1))))
# 342 + 469 = 811
c = addTwoNumbers(a,b)
while c.val is not None:
    print(c.val)            # 从低位开始输出，因为链表本身按照逆序存储。
    c = c.next

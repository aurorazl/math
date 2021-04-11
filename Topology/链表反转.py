
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
#迭代
def reverseChain(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
# 递归
def reverseChain2(head):
    if not head or not head.next:
        return head
    newHead = reverseChain2(head.next)
    head.next.next = head
    head.next = None            # 这一步可以避免造成最后一节和倒数第二环的闭环
    return newHead

a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
a = reverseChain2(a)
while a.next:
    print(a.val)
    a = a.next
print(a.val)


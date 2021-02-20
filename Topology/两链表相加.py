class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next=next

def addTwoNumbers(l1,l2):
    carry=0
    p,q = l1,l2
    c = Node()
    curr = c
    while p and q:
        x = p.val
        y = q.val
        sum_x_y = carry+x+y
        carry = sum_x_y//10
        curr.val = sum_x_y%10
        curr.next = Node()
        curr = curr.next
        p = p.next
        q = q.next
    return c

a = Node(2,Node(4,Node(3)))
b = Node(5,Node(6,Node(4)))
c = addTwoNumbers(a,b)
while c.val is not None:
    print(c.val)
    c = c.next

# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 思想： 二分、归并排序

# 技巧：快慢指针
"""
1、判定链表中是否含有环
用两个指针，一个跑得快(每次跑两步)，一个跑得慢。如果不含有环，跑得快的那个指针最终会遇到 null，说明链表不含环；如果含有环，快指针最终会超慢指针一圈，和慢指针相遇，说明链表含有环。
if (fast == slow) return true;
2.寻找链表的中点
让快指针一次前进两步，慢指针一次前进一步，当快指针到达链表尽头时，慢指针就处于链表的中间位置。
当链表的长度是奇数时，slow 恰巧停在中点位置；如果长度是偶数，slow 最终的位置是中间偏右：
while (fast != null && fast.next != null) {
        fast = fast.next.next;
        slow = slow.next;
        if (fast == slow) break;
    }
3.寻找链表的倒数第 k 个元素
使用快慢指针，让快指针先走 k 步，然后快慢指针开始同速前进。
while (k--> 0)
    fast = fast.next;
while (fast != null) {
    slow = slow.next;
    fast = fast.next;
}
4.已知链表中含有环，返回这个环的起始位置
相遇后，slow从head开始走，hight再走,只需一起走k-m步，大家都在环起点相遇了。
slow = head;
    while (slow != fast) {
        fast = fast.next;
        slow = slow.next;
    }
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # cut the LinkedList at the mid index.
        slow,fast = head,head.next           # slow = fast = head会让偶数个的链表中点slow偏右。
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right        # 然后将另一个没有遍历完的链表接上即可。
        return res.next
a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
Solution().sortList(a)
while a.next:
    print(a.val)
    a = a.next
print(a.val)
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        lst=[]
        while head:
            lst.append(head.val)
            head = head.next
        head = dummy
        for i in range(len(lst)-1,-1,-1):
            head.val = lst[i]
            head = head.next
        head = dummy
        return head
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
head=ListNode(10)
head.next=ListNode(3)
head.next.next=ListNode(7)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
sol = Solution()
sol.reverseList(head)
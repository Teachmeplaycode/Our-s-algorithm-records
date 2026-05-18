from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=slow=head
        while fast:
            print(fast.val, slow.val)
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
sol = Solution()
print(sol.hasCycle(head))
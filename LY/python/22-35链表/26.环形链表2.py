# class ListNode:
from typing import Optional
class ListNode:
    def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        while head != fast:
            head = head.next
            fast = fast.next
        return head
class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # 此时相遇
                p1 = slow
                p2 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p2
        return None
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
sol = Solution()
print(sol.detectCycle(head).val)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1: 
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:  
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution()
print(sol.removeNthFromEnd(head, 1))
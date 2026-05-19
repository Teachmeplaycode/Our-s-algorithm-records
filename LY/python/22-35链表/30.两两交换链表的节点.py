from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        dummy = head
        p = dummy
        while p and p.next:
            p.val,p.next.val = p.next.val,p.val
            if p.next.next is None: break
            p = p.next.next
        p = dummy
        # while p:
        #     print(p.val)
        #     p = p.next
        return p
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# sol = Solution()
# print(sol.swapPairs(head))
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:return head
        dummy = ListNode(0)
        new_p = dummy
        p = head
        while p:
            lst = []
            for _ in range(k):
                if not p:
                    break
                lst.append(p)
                p = p.next
            if len(lst) == k:
                lst.reverse()
                for i in range(k):
                    lst[i].next = lst[i+1] if i+1 < k else None
                new_p.next = lst[0]
                new_p = lst[-1]
            else:
                if lst:new_p.next = lst[0]
                break
        # new_p = dummy.next
        # while new_p:
        #     print(new_p.val)
        #     new_p = new_p.next
        return dummy.next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution()
print(sol.reverseKGroup(head, 3))
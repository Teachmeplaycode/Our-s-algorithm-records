from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from queue import PriorityQueue
class Wrapper:
    def __init__(self,node:ListNode):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        p = head
        q = PriorityQueue()
        while p: 
            q.put(Wrapper(p))
            p = p.next
        dummy = ListNode()
        newHead = dummy
        while not q.empty():
            top = q.get().node
            top.next = None
            newHead.next = top
            newHead = newHead.next
        return dummy.next
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
sol = Solution()
print(sol.sortList(head))
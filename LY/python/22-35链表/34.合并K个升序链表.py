from typing import List, Optional
from queue import PriorityQueue
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Wrapper:
    def __init__(self, node:ListNode):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        pq = PriorityQueue()
        for i in range(len(lists)):
            while lists[i]: 
                pq.put(Wrapper(lists[i]))
                lists[i] = lists[i].next
        dummy = ListNode(0)
        head = dummy
        while not pq.empty():
            top = pq.get().node
            top.next = None
            head.next = top
            head = head.next
        head = dummy.next
        # while head:
        #     print(head.val,end=" ")
        #     head = head.next
        return dummy.next
linklist1 = ListNode(1, ListNode(4, ListNode(5)))
linklist2 = ListNode(1, ListNode(3, ListNode(4)))
linklist3 = ListNode(2, ListNode(6))
lists = []
sol = Solution()
sol.mergeKLists(lists)
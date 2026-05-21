from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        while p:
            p.next = Node(p.val,p.next)
            p = p.next.next
        p = head
        while p:
            if p.random: p.next.random = p.random.next
            p = p.next.next
        p = dummy = Node(0,head)
        while p.next:
            p.next = p.next.next
            p = p.next
        return dummy.next
        
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.random = head.next.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next
head.next.next.next.next.random = head.next.next
sol = Solution()
print(sol.copyRandomList(head))
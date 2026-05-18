# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:     
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = []
        while l1:
            if l2 is None:l2 = ListNode(0)
            l1.val += l2.val
            list3.append(l1.val)
            l1 = l1.next
            l2 = l2.next
        while l2:
            if l1 is None:l1 = ListNode(0)
            l2.val += l1.val
            list3.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        list3.append(0)
        for i in range(len(list3)):
            if list3[i] >= 10:
                list3[i] -= 10
                list3[i+1] += 1
        if list3[-1] == 0:list3.pop()
        dummy = ListNode(-1)
        l3 = dummy
        for i in range(len(list3)):
            l3.next = ListNode(list3[i])
            l3 = l3.next
        return dummy.next
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l2 = ListNode(9)
sol = Solution()
sol.addTwoNumbers(l1,l2)
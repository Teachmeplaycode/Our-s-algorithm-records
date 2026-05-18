from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        lenA, lenB = 0, 0
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next
        currA, currB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next
        while currA and currB:
            if currA is currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None  
            
        
intersectVal = 8
listA = ListNode(4)    
listA.next = ListNode(1)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(4)
listA.next.next.next.next = ListNode(5)
listB = ListNode(5)
listB.next = ListNode(8)
listB.next.next = ListNode(4)
listB.next.next.next = ListNode(5)
sol = Solution()
print(sol.getIntersectionNode(listA,listB))
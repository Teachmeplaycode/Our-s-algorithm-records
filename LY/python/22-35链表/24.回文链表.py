from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(len(lst)//2):
            if lst[i] != lst[-i-1]:
                return False
        return True    
head = ListNode(1)
head.next = ListNode(2)
sol = Solution()
print(sol.isPalindrome(head))
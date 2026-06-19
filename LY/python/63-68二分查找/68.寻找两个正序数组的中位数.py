from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1,p2=0,0
        lst = []
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]<nums2[p2]:
                lst.append(nums1[p1])
                p1+=1
            else:
                lst.append(nums2[p2])
                p2+=1
        while p1<len(nums1):
            lst.append(nums1[p1])
            p1+=1
        while p2<len(nums2):
            lst.append(nums2[p2])
            p2+=1
        mid = len(lst)//2
        if len(lst)%2==0:
            return (lst[mid]+lst[mid-1])/2
        else:return float(lst[mid])
sol = Solution()
nums1 = [2,2,4,4]
nums2 = [2,2,2,4,4]
print(sol.findMedianSortedArrays(nums1,nums2))
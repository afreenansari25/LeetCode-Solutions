import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        curr = head
        
        while curr:
            len += 1
            curr = curr.next
            
        for i in range(len//2):
            head = head.next
            
        return head
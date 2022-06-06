import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        curr = node = head
        
        while curr:
            len += 1
            curr = curr.next
            
        l = len//2 #if len % 2 != 0 else len//2 + 1 
        #print(l)
            
        for i in range(l):
            node = node.next
            
        return node
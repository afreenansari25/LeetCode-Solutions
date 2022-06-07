# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        # Find mid of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        mid = slow
        
        # Reverse 1st half of the list
        prev, cur = None, mid
        while cur: 
            nxt = cur.next 
            cur.next = prev
            prev = cur
            cur = nxt
            
        # Compare both the lists
        l, r = head, prev
        
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
        
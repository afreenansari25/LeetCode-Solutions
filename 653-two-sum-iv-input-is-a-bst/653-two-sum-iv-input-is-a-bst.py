# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:            
        seen = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            val = k - node.val
            
            if val in seen:
                return True
            else:
                seen.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
        
        
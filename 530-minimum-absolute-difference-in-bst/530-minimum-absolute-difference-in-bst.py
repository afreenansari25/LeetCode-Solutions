# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        
        def in_order(root):
            if root:
                in_order(root.left)
                res.append(root.val)
                in_order(root.right)
            
        in_order(root)        
        
        return min(b-a for a,b in zip(res, res[1:]))
            
    
        

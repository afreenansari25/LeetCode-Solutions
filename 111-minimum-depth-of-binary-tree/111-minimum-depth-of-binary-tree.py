# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        '''
        # recursive approach
        
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        '''
        
        # iterative approach
        if not root:
            return 0 
        
        q = [root]
        depth = 0
        
        while q:
            n = len(q)
            depth += 1
            
            for i in range(n):
                node = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
                if not node.left and not node.right:
                    return depth
                
            
            
            
        
        
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        q = [root]
        res = []
        
        while q:
            val = []
            child = []
            
            for node in q:
                val.append(node.val)
                
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            q = child                    
            res.append(sum(val)/len(val))
            
        return res
        
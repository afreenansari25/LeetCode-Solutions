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
        
        res = []
        queue = [root]
        
        while queue:
            val, child = [], []
            
            for i in queue:
                
                val.append(i.val)
                if i.left:
                    child.append(i.left)
                if i.right:
                    child.append(i.right)
            
            queue = child
            res.append(sum(val)/len(val))
        
        return res
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if  node.left:
                if node.val == node.left.val:
                    q.append(node.left)
                else:
                    return False
            if node.right:
                if node.val == node.right.val:
                    q.append(node.right)
                else:
                    return False
        return True
                
        
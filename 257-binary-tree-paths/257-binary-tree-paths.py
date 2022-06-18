# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        
        def dfs(root, ls, res):
            print(ls)
            if not root.left and not root.right:
                res.append(ls+str(root.val))
                
            if root.left:
                dfs(root.left, ls+str(root.val)+"->", res)
            if root.right:
                dfs(root.right, ls+str(root.val)+"->", res)
                
            return res
        
        return dfs(root, "", res)
        
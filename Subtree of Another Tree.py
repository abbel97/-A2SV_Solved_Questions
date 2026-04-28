# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(x,y):
            if not x or not y:
                return not x and not y
            return x.val == y.val and same(x.left,y.left) and same(x.right, y.right)
        def dfs(x, y):
            if same(x,y): 
                return True
            if not x:
                return False
            return dfs(x.left, y) or dfs(x.right, y)
        return dfs(root, subRoot)
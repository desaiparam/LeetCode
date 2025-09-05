# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.maxDepth = 0
        def dfs(root,depth):
            if not root:
                return 
            if self.maxDepth < depth:
                self.maxDepth = depth
                self.ans = root.val
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        return self.ans
                
        
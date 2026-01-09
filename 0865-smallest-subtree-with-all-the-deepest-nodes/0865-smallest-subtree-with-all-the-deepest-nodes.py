# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        def dfs(root):
            if not root:
                return 0,None
            leftdepth,leftnode = dfs(root.left)
            rightdepth,rightnode = dfs(root.right)
            if leftdepth > rightdepth:
                return (leftdepth+1,leftnode)
            elif leftdepth < rightdepth:
                return (rightdepth+1,rightnode)
            return (rightdepth+1,root)
        return dfs(root)[1]

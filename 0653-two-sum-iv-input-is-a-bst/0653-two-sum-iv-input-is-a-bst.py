# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        self.seen = set()
        def dfs(root):
            if root is None:
                return False
            if k - root.val in self.seen:
                return True
            self.seen.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)

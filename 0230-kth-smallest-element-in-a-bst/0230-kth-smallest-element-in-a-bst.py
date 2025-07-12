# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        self.count = 0
        self.res = None
        def helper(root):
            if root is None:
                return 0
            helper(root.left)
            self.count += 1
            if k == self.count:
                self.res = root.val
                return 
            helper(root.right)
        helper(root)
        return self.res
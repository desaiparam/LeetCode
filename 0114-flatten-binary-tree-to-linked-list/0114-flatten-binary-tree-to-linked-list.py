# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def helper(root):
            nonlocal prev
            if root is None:
                return 
            # print(root.val)
            helper(root.right)
            helper(root.left)
            root.right = prev
            root.left = None
            prev = root
        helper(root)
        # return prev

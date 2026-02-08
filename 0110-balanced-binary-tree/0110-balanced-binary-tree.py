# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            lefty = check(root.left)
            righty = check(root.right)
            if lefty == -1 or righty == -1 or abs(lefty-righty) > 1:
                return -1
            return 1 + max(lefty,righty)
        return check(root)  != -1

        
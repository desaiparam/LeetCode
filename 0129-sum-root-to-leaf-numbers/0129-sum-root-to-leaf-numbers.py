# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        if not root:
            return 0
        def helper(root,sumy):
            if not root.left and not root.right:
                self.total += root.val+sumy*10
                return 
            if  root.left:
                helper(root.left,root.val+sumy*10)
            if  root.right:
                helper(root.right,root.val+sumy*10)
        helper(root,0)
        return self.total
        

        
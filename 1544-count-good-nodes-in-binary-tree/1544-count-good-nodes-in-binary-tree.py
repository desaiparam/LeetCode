# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,max_so_far):
            if not root:
                return 0
            good = 1 if root.val >= max_so_far else 0

            max_so_far = max(max_so_far,root.val)
            good += helper(root.left,max_so_far)
            good += helper(root.right,max_so_far)
            return good
        return helper(root,float('-inf'))
                
        
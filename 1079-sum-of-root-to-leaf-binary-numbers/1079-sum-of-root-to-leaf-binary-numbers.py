# from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preOrder(root , path):
            if not root:
                return 0
            path = (path<<1) + root.val
            if not root.left and not root.right:
                return path
            return preOrder(root.left,path) + preOrder(root.right,path)
        return preOrder(root,0)        
        
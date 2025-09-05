# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def helper(root):
            if root == None:
                return 0
            lefty = helper(root.left)
            righty = helper(root.right)
            self.ans = max(self.ans,lefty+righty)
            print(self.ans)
            return 1 + max(lefty,righty)
        helper(root)
        return self.ans
        
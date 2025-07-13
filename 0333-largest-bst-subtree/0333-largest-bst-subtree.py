# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_size = 0
        def helper(root):
            if root is None:
                return (True, 0, float('-inf'), float('inf'))
            left_bst,left_size,left_maxi,left_mini = helper(root.left)
            right_bst,right_size,right_maxi,right_mini = helper(root.right)
            if left_bst and right_bst and left_maxi < root.val < right_mini:
                size = left_size + right_size + 1
                self.max_size = max(size,self.max_size)
                return (True,size,max(right_maxi,root.val),min(left_mini,root.val))
            else:
                return (False,0,0,0)
        helper(root)
        return self.max_size

        
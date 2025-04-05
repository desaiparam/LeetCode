# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def vali(root):
            if not root:
                return 0
            left = vali(root.left)
            right = vali(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1: #check if left or right is less than 1 and the sub btwn them is greater than 1 
                return -1
            return max(left,right) + 1 #return which ever is bigger with +1
        return vali(root) != -1


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(root):
            if not root:
                return (0,0)
            left_inc,left_dec = dfs(root.left)
            right_inc,right_dec = dfs(root.right)
            inc,dec = 1,1
            if root.left: 
                if root.left.val+1 == root.val:
                    inc = max(inc,left_inc+1)
                elif root.left.val-1 == root.val:
                    dec = max(dec,left_dec+1)
            if root.right:
                if root.right.val+1 == root.val:
                    inc = max(inc,right_inc+1)
                elif root.right.val -1 == root.val:
                    dec = max(dec,right_dec+1)
            self.total = max(self.total,inc+dec-1)
            return (inc,dec)
        dfs(root)
        return self.total
            
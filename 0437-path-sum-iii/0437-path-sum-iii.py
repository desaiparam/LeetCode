# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        freq = {0:1}
        def helper(root,curr):
            if not root:
                return 
            curr += root.val
            self.count += freq.get(curr-targetSum,0)
            freq[curr] = freq.get(curr,0) + 1
            helper(root.left,curr)
            helper(root.right,curr)
            freq[curr] -= 1
        helper(root,0)
        return self.count



        
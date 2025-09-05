# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #TC O(N) SC O(N+h)
        # res = []
        # def helper(root):
        #     if not root:
        #         return []
        #     helper(root.left)
        #     res.append(root.val)
        #     helper(root.right)
        # helper(root)
        # return res[k-1]
        # TC O(h+k) SC O(h)
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr=curr.right

        
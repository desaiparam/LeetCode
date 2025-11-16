# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(root):
            if not root:
                return -1
            leftroot = dfs(root.left)
            rightroot = dfs(root.right)
            height = 1 + max(leftroot,rightroot)
            if height == len(ans):
                ans.append([])
            ans[height].append(root.val)
            return height
        dfs(root)
        return ans 

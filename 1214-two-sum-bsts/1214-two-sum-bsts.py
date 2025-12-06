# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        remaining = 0
        ar = []
        br = []
        def dfs(root,lis):
            if not root:
                return
            lis.append(root.val)
            dfs(root.left,lis)
            dfs(root.right,lis)
        dfs(root1,ar)
        dfs(root2,br)
        ar.sort()
        br.sort()
        l = 0
        r = len(br) - 1
        while l < len(ar) and r >= 0:
            if ar[l] + br[r] == target:
                return True
            elif ar[l] + br[r] < target:
                l += 1
            else:
                r -= 1
        return False
                

        # print(ar,br)
        


        

       
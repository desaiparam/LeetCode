# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        def helper(root,level):
            if not root:
                return []
            if level == len(ans):
                print(level,root.val)
                ans.append(root.val)
            # right will come first as we need to check the right side first 
            # if question changes to left view left side would be first
            helper(root.right,level+1)
            helper(root.left,level+1)
        helper(root,0)
        return ans 

        
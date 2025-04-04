# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inset(root,val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = inset(root.left,val)
            else:
                root.right = inset(root.right,val)
            return root
        return inset(root,val)
        
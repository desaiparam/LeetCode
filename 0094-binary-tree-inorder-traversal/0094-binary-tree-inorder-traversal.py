# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(node):
            if node is not None:
               return inOrder(node.left)+[node.val]+inOrder(node.right)
            else:
                return []
        return inOrder(root)
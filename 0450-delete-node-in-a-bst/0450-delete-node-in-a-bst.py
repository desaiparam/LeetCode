# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            min_root = root.right
            while min_root.left:
                min_root = min_root.left
            root.val = min_root.val
            root.right = self.deleteNode(root.right,min_root.val)
        return root
    
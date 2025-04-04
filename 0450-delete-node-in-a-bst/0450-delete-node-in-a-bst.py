# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def change(root):
            while root.left:
                root = root.left
            return root
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
        #this is to reomve the extra node
            min_val=change(root.right)
            root.val = min_val.val
            root.right = self.deleteNode(root.right,min_val.val)

        return root


        
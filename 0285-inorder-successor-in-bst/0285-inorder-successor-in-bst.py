# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorderList = []
        def inorder(root):
            if not root:
                return None
            left = inorder(root.left)
            inorderList.append(root)
            right = inorder(root.right)
            return inorderList
        inorder(root)
        for i in range(len(inorderList)-1):
            if inorderList[i] == p:
                return inorderList[i+1]
        return None
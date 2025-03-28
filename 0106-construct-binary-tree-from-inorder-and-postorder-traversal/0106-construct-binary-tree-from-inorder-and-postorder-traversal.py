# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #Solution 1 T.C:-O(N^2)
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:],postorder)
        root.left = self.buildTree(inorder[:idx],postorder)
        return root



        #Solution 2 T.C:-O(N)
        # def helper(l,r):
        #     if l > r :
        #         return None
        #     root = TreeNode(postorder.pop())
        #     # root = TreeNode(val)
        #     # index = ima[val]
        #     index = ima[root.val]
        #     root.right = helper(index + 1, r)
        #     root.left = helper(l, index - 1)
        #     return root
        # ima = {val: idx for idx, val in enumerate(inorder)}
        # return helper(0, len(inorder) - 1)
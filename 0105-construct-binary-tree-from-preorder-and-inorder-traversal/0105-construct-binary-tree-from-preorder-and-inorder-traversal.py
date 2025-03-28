# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       #Solution 1 T.C:-O(N^2)
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0]) 
        # root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # return root

        #Solution 2 T.C:-O(N)
        def helper(l,r):
            if l>r:
                return None
            root = TreeNode(preorder.pop(0))
            index = has[root.val]
            root.left = helper(l,index-1)
            root.right = helper(index+1,r)
            return root


        has = {v:i for i,v in enumerate(inorder)}
        return helper(0,len(inorder)-1)
        
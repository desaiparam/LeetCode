# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
        def bst(left,right):
            if left > right:
                return None
            mid = (left + right) //2
            root = arr[mid]
            root.left = bst(left,mid-1)
            root.right = bst(mid+1,right)
            return root
        inorder(root)
        # print(arr)
        return bst(0,len(arr)-1)

            
            


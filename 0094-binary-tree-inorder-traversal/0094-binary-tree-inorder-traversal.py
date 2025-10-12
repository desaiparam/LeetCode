# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        while curr:
            if  curr.left:
                predecessor = curr.left
                while predecessor.right  and predecessor.right != curr:
                    predecessor = predecessor.right
                if predecessor.right:
                    
                    predecessor.right = None
                    res.append(curr.val)
                    curr = curr.right
                else:
                    predecessor.right = curr
                    curr = curr.left
            else:
                res.append(curr.val)
                curr = curr.right
        return res

        
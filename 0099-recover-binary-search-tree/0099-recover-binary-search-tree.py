# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.sec = None
        self.prev = None
        def helper(root):
            if root is None:
                return 
            helper(root.left)
            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                self.sec = root
            self.prev = root
            helper(root.right)
           
        helper(root)
        print("before",self.first,self.sec)
        # self.first,self.sec = self.sec,self.first
        self.first.val, self.sec.val = self.sec.val, self.first.val
        print("after",self.first,self.sec)
        return root
                


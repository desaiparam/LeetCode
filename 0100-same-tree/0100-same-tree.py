# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Solution 1 reccursion
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)


        #Solution 2 iterative
        def check(p,q):
            if not p and not q:
                return True 
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        de = deque([(p,q),])
        while de:
            p,q = de.popleft()
            if not check(p,q):
                return False
            if p :
                de.append((p.left,q.left))
                de.append((p.right,q.right))
        return True
        
        
        
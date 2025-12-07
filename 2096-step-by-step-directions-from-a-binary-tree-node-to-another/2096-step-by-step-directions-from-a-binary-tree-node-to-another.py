# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        def findPath(root,target,path):
            if not root:
                return False
            path.append(root)
            if root.val == target:
                return True
            if findPath(root.left,target,path):
                return True
            if findPath(root.right,target,path):
                return True
            path.pop()
            return False
        pathStart = []
        pathDest = []
        findPath(root,startValue,pathStart)
        findPath(root,destValue,pathDest)
        i = 0
        while i < len(pathStart) and i < len(pathDest) and pathStart[i] == pathDest[i]:
            i += 1
        lca = i 
        parent = len(pathStart) - lca
        res = "U" * parent
        finalPath = ""
        for j in range(lca,len(pathDest)):
            p = pathDest[j - 1]
            ch = pathDest[j]
            if p.left == ch:
                finalPath += "L"
            if p.right == ch:
                finalPath += "R"
        answer = res + finalPath
        return answer


        
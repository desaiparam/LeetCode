# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(root,sumy,path):
            if not root:
                return 
            sumy += root.val
            path.append(root.val)
            if not root.left and not root.right and sumy == targetSum:
                result.append(path[:])
            dfs(root.left,sumy,path)
            dfs(root.right,sumy,path)
            path.pop()
        dfs(root,0,[])
        return result
        
            
        
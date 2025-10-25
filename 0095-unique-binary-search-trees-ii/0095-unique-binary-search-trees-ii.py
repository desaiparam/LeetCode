# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start,end):
            result = []
            if start > end:
                return [None]
            for i in range(start,end+1):
                left = helper(start,i-1)
                right = helper(i+1,end)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
                # print(result)
            return result
       
        return  helper(1,n)
        

        
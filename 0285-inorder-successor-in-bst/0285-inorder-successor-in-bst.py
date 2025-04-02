# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorderList = []
        findItem = 0
        def inorder(root,count):
            if not root:
                return None
            # if root.val == p.val: 
            #     inorderList.append(root.val)
            #     # findItem = count
            #     return count
            #     # continue
            left = inorder(root.left,count+1)
            inorderList.append(root)
            right = inorder(root.right,count+1)
            return inorderList
        inorder(root,0)
        # print(inorderList)
        # print(findItem)
        ans = 0
        # for i in inorderList:
        #     if i == p.val:
        #         print(i+1)
        #         ans = i+1
        # return ans
        for i in range(len(inorderList)-1):
            if inorderList[i] == p:
                return inorderList[i+1]
        return None
                # return ans 
        # for index, value in enumerate(inorderList):
        #     if value == p.val:  # Compare the value of TreeNode p with the value in the list
        #         ans = index + 1  # Store the position in ans (1-based index)
        #         return ans

            


        
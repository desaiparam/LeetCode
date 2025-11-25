# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = ','
    NIL = '#'
    def serialize(self, root):
        if not root:
            return self.NIL
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                out.append(self.NIL)
                continue
            out.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
            i = len(out) - 1
            while i >= 0 and out[i] == self.NIL:
                i -= 1
        return self.SEP.join(out[:i+1]) if i >= 0 else self.NIL
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if not data or data == self.NIL:
            return None 
        vals = data.split(self.SEP)
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            parent = q.popleft()
            if i < len(vals):
                if vals[i] != self.NIL:
                    left = TreeNode(int(vals[i]))
                    parent.left = left
                    q.append(left)
                i += 1
            if i < len(vals):
                if vals[i] != self.NIL:
                    right = TreeNode(int(vals[i]))
                    parent.right = right
                    q.append(right)
                i += 1
        return root

                
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
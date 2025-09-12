"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        self.res = []
        if not root:
            return ""
        def dfs(root):
            for i in (root.children or []):
                dfs(i)
            self.res.append(str(root.val))
            self.res.append(str(len(root.children or [])))
        dfs(root)
        print(" ".join(self.res))
        return " ".join(self.res)
        

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        res = data.split()
        stack = []
        for i in range(0,len(res),2):
            val = int(res[i])
            k  = int(res[i+1])
            root = Node(val,[])
            if k:
                child = stack[-k:]
                stack[-k:] = []
                root.children.extend(child)
            stack.append(root)
        return stack[-1]
            


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
class Trie:
    def __init__(self):
        self.children = {}
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Trie()

        for i in arr1:
            node = root
            for j in str(i):
                if j not in node.children:
                    node.children[j] = Trie()
                node = node.children[j]
        longest = 0
        for i in arr2:
            node = root
            count = 0
            for j in str(i):
                if j not in node.children:
                    break
                node = node.children[j]
                count += 1
            longest = max(longest,count)
                
        return longest
        
class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class Solution:
    def __init__(self):
      self.root = TrieNode()
      self.result = ""
    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            # if i in node:
            index = ord(i) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.endOfWord = True
    def longestWord(self, words: List[str]) -> str:
        for w in words:
            self.insert(w)
        
        def dfs(curr,path):
            if len(path) > len(self.result):
                self.result = "".join(path)
            for i in range(26):
                if curr.children[i] and curr.children[i].endOfWord:
                    length = len(path)
                    path.append(chr(i + ord('a')))
                    dfs(curr.children[i],path)
                    path = path[:length]
        dfs(self.root,[])
        return self.result



        
        
class TrieNode():
    def __init__(self):
        self.arr = [None] * 26
        self.EndOfWord= False

class Trie:
    def __init__(self):
      self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            # if i in node:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                node.arr[index] = TrieNode()
            node = node.arr[index]
        node.EndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                return False
            node = node.arr[index]
        return node.EndOfWord
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                return False
            node=node.arr[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
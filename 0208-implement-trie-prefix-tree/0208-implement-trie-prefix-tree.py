class TrieNode():#Creating a array to store characters and to check when we reach end of the word
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
            index = ord(i) - ord('a')#this checks the index of the character
            if not node.arr[index]:#if not in arr we will insert in the trie
                node.arr[index] = TrieNode()
            node = node.arr[index]
        node.EndOfWord = True#the word is completed

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            index = ord(i) - ord('a')
            if not node.arr[index]:#not found in the array 
                return False
            node = node.arr[index]#if found check 
        return node.EndOfWord
            
    def startsWith(self, prefix: str) -> bool:#same logic as search just return True 
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
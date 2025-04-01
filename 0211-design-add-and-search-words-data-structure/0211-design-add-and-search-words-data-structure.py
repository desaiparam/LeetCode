class TrieNode():
    def __init__(self):
        self.arr = [None] * 26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                node.arr[index] = TrieNode()
            node = node.arr[index] 
        node.endOfWord = True       

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if len(word) == i:
                return node.endOfWord
            char = word[i]
            if char == '.':
                for j in node.arr:
                    if j and dfs(j,i+1):
                        return True
                return False
            else:
                index = ord(char) - ord('a')
                if not node.arr[index]:
                    return False
                # node = node.arr[index]
                return dfs(node.arr[index],i+1)
        return dfs(self.root,0)

                

            
        # node = self.root
        # for i in word:
        #     if i == '.':
        #         # print(i)
        #         break
        #     index = ord(i) - ord('a')
        #     if not node.arr[index]:
        #         print(i)
        #         return False
        #     node = node.arr[index]
        # return node.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
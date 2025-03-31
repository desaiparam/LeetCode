class TrieNode():
    def __init__(self):
        self.arr = [None] * 26
        self.endOfWord = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,s:str):
        node = self.root
        for i in s:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                node.arr[index] = TrieNode()
            node = node.arr[index]
        node.endOfWord = True
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for i in dictionary:
            self.insert(i)

        word = sentence.split()
        # print(word)
        ans = []
        for i in word:
            node = self.root
            pre = ''
            ifexsist = False
            for j in i:
                index = ord(j) - ord('a')
                if not node.arr[index]:
                    break
                node = node.arr[index]
                pre += j
                # print(j)
                if node.endOfWord:
                    ifexsist = True
                    break
            
            if ifexsist:
                ans.append(pre)
            else:
                ans.append(i)
        return " ".join(ans)

            
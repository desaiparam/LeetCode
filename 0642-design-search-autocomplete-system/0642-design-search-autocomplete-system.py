class TrieNode:
    def __init__(self):
        self.children = [None] * 256
        self.top3 = []
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.search = ""
        self.map = {}
        for i in range(len(sentences)):
            self.map[sentences[i]]  = self.map.get(sentences[i],0) + times[i]
            self.insert(sentences[i])
    def insert(self,word):
        curr=self.root  
        for i in word:
            idx = ord(i) - ord(' ')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr=curr.children[idx]
            l = curr.top3
            if word not in l:
                l.append(word)
            l.sort(key=lambda x:(-self.map[x],x))
            if len(l)>3:
                l.pop()
    def searchP(self,prefix):
        curr = self.root
        for i in prefix:
            idx = ord(i) - ord(' ')
            if curr.children[idx] is None:
                return []
            curr = curr.children[idx]
        return curr.top3

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.map[self.search] = self.map.get(self.search,0) + 1
            self.insert(self.search)
            self.search = ""
            return []
        self.search += c
        return self.searchP(self.search)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
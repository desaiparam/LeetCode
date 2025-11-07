class TrieNode:
    def __init__(self):
        self.arr = [None] * 26
        self.eod = False
        self.word = None
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for i in word:
            char = ord(i) - ord('a')
            if not node.arr[char]:
                node.arr[char] = TrieNode()
            node = node.arr[char]
        node.eod = True 
        node.word = word 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # TLE O(N*M*4^L)
        # n = len(board)
        # m = len(board[0])
        # res = []
        # seen = set()
        # def back(i,j,word,lenW,curr):
        #     if 0 > i or i >= n or 0 > j or j >=  m:
        #         return False
        #     if board[i][j] != word[curr]:
        #         return False
        #     if curr == lenW-1  and board[i][j] == word[curr]:
        #         return True
        #     char = word[curr]
        #     found = False
        #     if char == board[i][j]:
        #         temp = board[i][j]
        #         board[i][j] = "."
        #         found = (back(i+1,j,word,lenW,curr+1) or
        #         back(i,j+1,word,lenW,curr+1) or
        #         back(i-1,j,word,lenW,curr+1) or
        #         back(i,j-1,word,lenW,curr+1))
        #         board[i][j] = temp
        #     return found
        # for k in words:
        #     for i in range(n):
        #         for j in range(m): 
        #             if back(i,j,k,len(k),0):
        #                 if k in seen:
        #                     continue
        #                 seen.add(k)
        #                 res.append(k)
        # return res
        for i in words:
            self.insert(i)
        n = len(board)
        m = len(board[0])
        res = []
        seen = set()
        node = self.root
        def dfs(i,j,node):
            if 0 > i or i >= n or 0 > j or j >=  m:
                return False
            # if board[i][j] != word[curr]:
            #     return False 
            char = ord(board[i][j]) - ord('a')

            if board[i][j] == "." or not node.arr[char]:
                return 
            node = node.arr[char]  
            if node.eod:
                if node.word not in seen:
                    seen.add(node.word)
                    res.append(node.word)
            temp = board[i][j] 
            board[i][j] = "."
            dfs(i-1,j,node)
            dfs(i+1,j,node)
            dfs(i,j+1,node)
            dfs(i,j-1,node)
            board[i][j]=temp
        for i in range(n):
            for j in range(m): 
                if self.root.arr[ord(board[i][j]) - ord('a')]:
                    dfs(i,j,self.root)

        return res

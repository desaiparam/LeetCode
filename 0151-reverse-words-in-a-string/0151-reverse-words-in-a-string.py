class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        print(word)
        for i in word:
            rs = word[::-1]
        return " ".join(rs)
        
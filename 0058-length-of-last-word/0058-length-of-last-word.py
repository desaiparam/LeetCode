class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spl = s.split()
        print(spl[-1])
        return len(spl[-1])
         
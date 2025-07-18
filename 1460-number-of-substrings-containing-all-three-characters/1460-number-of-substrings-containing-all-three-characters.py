class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = [-1, -1, -1]
        count = 0
        for i in range(len(s)):
            lastseen[ord(s[i]) - ord('a')] = i
            if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:
                count = count + (1+min(lastseen[0],lastseen[1],lastseen[2]))
        return count

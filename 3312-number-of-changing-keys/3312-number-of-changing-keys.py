class Solution:
    def countKeyChanges(self, s: str) -> int:
        l_s = s.lower()
        print(l_s)
        count = 0
        key = l_s[0]
        for i in range(len(l_s)):
            if ord(l_s[i])- ord('a') != ord(key)-ord('a') :
                key=l_s[i]
                count+=1
        return count
        
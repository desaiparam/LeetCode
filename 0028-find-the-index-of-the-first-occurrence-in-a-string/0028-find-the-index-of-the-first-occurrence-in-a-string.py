class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        if not needle :
            return -1
        while i<=len(haystack) - len(needle):
            j=0
            while j<len(needle) and haystack[i+j] == needle[j]:
                j+=1
            if j==len(needle):
                return i
            i+=1
        return -1        
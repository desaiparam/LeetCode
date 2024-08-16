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
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:  # Edge case: if needle is empty, return 0
#             return 0
        
#         i = 0
#         while i <= len(haystack) - len(needle):
#             j = 0
#             while j < len(needle) and haystack[i + j] == needle[j]:
#                 j += 1
#             if j == len(needle):  # If the entire needle is found
#                 return i
#             i += 1
        
#         return -1  # Return -1 if needle is not found in haystack

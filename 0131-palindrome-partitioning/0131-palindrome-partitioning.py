class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(path,idx):
            if len(s) == idx:
                ans.append(path[:])
                return 
            for i in range(idx,len(s)):
                if palindrome(s,idx,i):   
                    path.append(s[idx:i+1]) 
                    backtrack(path,i+1)
                    path.pop()
        def palindrome(path,start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        backtrack([],0)
        return ans


        
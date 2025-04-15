class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        def helper(index,s,path,ans):
            if index == len(s):
                ans.append(path[:])
                return 
            for i in range(index,len(s)):
                if isPalindrom(s,index,i):
                    path.append(s[index:i+1])
                    helper(i+1,s,path,ans)
                    path.pop()

        def isPalindrom(s,start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        helper(0,s,path,ans)
        return ans
        
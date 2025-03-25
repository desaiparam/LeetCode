class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(i,s,n):
            if i >= n/2:
                return 
            s[i],s[n-i-1] = s[n-i-1],s[i]
            helper(i+1,s,n)
        n = len(s)
        helper(0,s,n)
        
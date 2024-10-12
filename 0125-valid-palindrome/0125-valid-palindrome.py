class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = re.sub('[^a-zA-Z0-9]', '', s).lower()
        print("s_alpha",s_alpha)
        i = 0
        j = len(s_alpha)-1
        while i < j:
            print(s_alpha[i],s_alpha[j])
            if s_alpha[i] != s_alpha[j] :
                return False
            i += 1
            j -= 1
        return True
        
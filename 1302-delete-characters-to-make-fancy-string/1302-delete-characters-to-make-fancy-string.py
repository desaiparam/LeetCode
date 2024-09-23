class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        char_list = []
        for i ,j in enumerate(s):
            if i > 0 and j == s[i-1]:
                count +=1
            else:
                count = 1
            if count<3:
                char_list.append(j)
        

        return ''.join(char_list)
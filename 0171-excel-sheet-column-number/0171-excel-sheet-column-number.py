class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res =0
        po =0
        for char in reversed(columnTitle):
            
            dig = ord(char)-64
           
            res += dig*26**po
            
            po+=1
        return res
         


             
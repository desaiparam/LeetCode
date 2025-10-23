class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        counter = 0
        while word * (counter + 1) in sequence:
            counter += 1
        return counter
        

            
        
        
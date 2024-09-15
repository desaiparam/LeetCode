class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        sets={}
        short_word =None
        shor_len = float("inf")
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                sets[char] = sets.get(char,0)+1
        for word in words:
            word_count = {}
            for char in word : 
                word_count[char] = word_count.get(char,0)+1
            is_Valid = True
            for char,freq in sets.items():
                if word_count.get(char,0) < freq:
                    is_Valid = False
                    break
            if is_Valid:
                if len(word)<shor_len:
                    shor_len = len(word)
                    short_word = word
                
        return short_word
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hashmap = {}
        self.dict = dictionary
        for i in self.dict:
            if len(i) <= 2:
                self.hashmap[i] = i
            else:
                abberivation = i[0] + str(len(i[1:-1])) + i[-1]
                if abberivation not in self.hashmap:
                    self.hashmap[abberivation] = i 
                else:
                    if self.hashmap[abberivation] != i:
                        self.hashmap[abberivation] = None 

    def isUnique(self, word: str) -> bool:
        newWord = word[0] + str(len(word[1:-1])) + word[-1]
        # print(word)
        # print(self.hashmap)
        # print(newWord)
        if newWord not in self.hashmap:
            return True
        elif self.hashmap.get(newWord) == word:
            return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
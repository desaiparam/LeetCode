class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.mapping = {}
        self.dict = dictionary
        # print(self.dict)
        # print(dictionary)
        for i in dictionary:
            if len(i) <= 2:
                self.mapping[i] = i
            else:
                ab = i[0] + str(len(i[1:-1])) + i[-1]
                if ab not in self.mapping:
                    self.mapping[ab] = i
                else:
                    self.mapping[ab] = None

    def isUnique(self, word: str) -> bool:
        # print(word)
        # pass
        # for i in word
        neeW = word[0] + str(len(word[1:-1])) + word[-1]
        # print(neeW)
        # print(self.mapping)
        # print(word)

        if neeW not in self.mapping:
            return True
        elif self.mapping.get(neeW) == word:
            return True
        return False



# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
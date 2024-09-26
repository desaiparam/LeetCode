class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_set = {}
        char_s = []
        sum = 0
        for i in range(len(keyboard)):
            key_set[keyboard[i]] = i
        # print(key_set)
        pre = list(key_set.values())[0]
        # print(pre)
        for char in word:
            char_s.append(char)
        # print(char_s)
        for char in char_s:
            if char in key_set:
                sum += abs(pre - key_set[char])
                pre = key_set[char]
                print("sum",sum)
                print("pre",pre)
        return sum
        
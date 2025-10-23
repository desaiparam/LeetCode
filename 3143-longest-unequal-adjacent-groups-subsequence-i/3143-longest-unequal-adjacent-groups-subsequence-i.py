class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = -1
        result = []
        for i in range(len(words)):
            if prev == groups[i]:
                continue
            else:
                prev = groups[i]
                result.append(words[i])
        return result
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)    
        dp = {}                

        for w in words:
            dp[w] = 1           

            for i in range(len(w)):
                pred = w[:i] + w[i+1:]
                if pred in dp:
                    dp[w] = max(dp[w], dp[pred] + 1)

        return max(dp.values())
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        long_str = 0
        for i in range(len(s)):
           
            if s[i]  in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1

            count = i - left + 1
            # print(count)
            # print("maxie values",max(seen.values()))
            # print("seen",seen)
            if count - max(seen.values()) <= k:
                long_str = max(long_str,count)
                # print(long_str)
            else:
                seen[s[left]] -= 1
                if not seen[s[left]]:
                    seen.pop(s[left])
                left += 1
            
        return long_str
            
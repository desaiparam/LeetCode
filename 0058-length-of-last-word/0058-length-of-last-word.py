class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m = re.search(r'\b\w+\b',s[::-1])
        if m:
            return len(m.group()[::-1])
        return 0
        
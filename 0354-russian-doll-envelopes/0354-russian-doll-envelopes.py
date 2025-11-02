class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        result = []
        n = len(envelopes)
        for i in envelopes:
            low = 0
            high = len(result)-1
            while low <= high:
                mid = low + (high - low) // 2
                if result[mid] < i[1] :
                    low = mid + 1
                else:
                    high = mid - 1
            if len(result) == low:
                result.append(i[1])
            else:
                result[low] =i[1]
        return len(result)

            
            
                
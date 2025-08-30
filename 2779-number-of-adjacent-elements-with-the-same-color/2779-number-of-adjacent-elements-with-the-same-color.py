class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        output = []
        pairs = [0] * n
        curr = 0
        for i , j in queries:
            old = pairs[i]
            pairs[i] = j
            # print(pairs)
            if i > 0  and pairs[i-1] != 0:
                if old != 0 and old == pairs[i-1]:
                    curr -= 1
                if j == pairs[i-1]:
                    curr += 1
                
            if i < n-1 and pairs[i+1] != 0:
                if old != 0 and old == pairs[i+1]:
                    curr -= 1
                if j == pairs[i+1]:
                    curr += 1
            output.append(curr)
        return output

        
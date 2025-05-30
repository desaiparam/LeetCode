class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            maxi = max(gifts)
            index = gifts.index(maxi)
            gifts[index] = int(math.sqrt(maxi))
            k -= 1
            # print(gifts)
        return sum(gifts)
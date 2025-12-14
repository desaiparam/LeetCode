class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        countseats = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                countseats.append(i)
        if len(countseats) == 0 or len(countseats) % 2 != 0:
            return 0
        if len(countseats) == 2:
            return 1
        ways = 1
        for i in range(2,len(countseats),2):
            # print("hgrfdsa")
            gap = countseats[i] - countseats[i-1]
            ways = (gap* ways) % MOD
        return ways
        
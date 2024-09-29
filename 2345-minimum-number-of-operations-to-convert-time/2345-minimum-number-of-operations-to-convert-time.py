class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur = 60 * int(current[0:2]) + int(current[3:5])
        tar = 60 * int(correct[0:2]) + int(correct[3:5])
        # print(cur)
        # print(tar)
        d = tar - cur
        step = 0
        print(d)
        for i in [60,15,5,1]:
            print(step,"step")
            step += d // i
            print("d",d)
            d %= i
        return step
       
        
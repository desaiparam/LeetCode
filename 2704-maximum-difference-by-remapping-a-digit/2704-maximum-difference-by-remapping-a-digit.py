class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_n = str(num)
        maxi = num
        mini = 0
        for i in str_n:
            if int(i)<9:
                maxi = int(str_n.replace(i,"9"))
                break
        for i in str(num):
            if int(i)>0:
                mini = int(str_n.replace(i,"0"))
                break
        return maxi-mini
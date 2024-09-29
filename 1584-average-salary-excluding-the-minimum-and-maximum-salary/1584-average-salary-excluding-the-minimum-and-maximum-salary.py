class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maxi = max(salary)
        # print(maxi)
        # print(mini)
        salary.remove(mini)
        salary.remove(maxi)
        # print(salary)
        sumy = sum(salary)
        return sumy/len(salary)
        
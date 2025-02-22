class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev = 0
        for i,j in brackets:
            if income >= i:
                tax += (i - prev) * j /100
                prev = i
            else:
                tax += (income - prev) * j /100
                return tax
        return tax


        
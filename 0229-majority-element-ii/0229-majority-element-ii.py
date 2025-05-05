class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        element1 = float('-inf')
        element2 = float('-inf')
        for i in nums:
            if count1 == 0 and i != element2:
                count1 = 1
                element1 = i
            elif count2 == 0 and i != element1:
                count2 = 1
                element2 = i
            elif i == element1 :
                count1 +=1
            elif i == element2:
                count2 +=1
            else:
                count1 -= 1
                count2 -= 1
        count1= 0
        count2 = 0
        for i in nums:
            if i == element1:
                count1+=1
            elif i == element2:
                count2+=1  
        result = []
        if count1 > len(nums)//3:
            result.append(element1)
        if count2 > len(nums)//3:
            result.append(element2)
        return result          
        
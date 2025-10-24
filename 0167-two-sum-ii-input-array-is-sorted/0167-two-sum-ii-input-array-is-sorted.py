class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result= {}
        for i in range(len(numbers)):
            carry = target - numbers[i]
            if carry in result:
                return [result[carry],i+1]
            result[numbers[i]] = i+1
        # i = 0
        # j = len(numbers) - 1
        # # print(j)
        # while i < j:
        #     print(i,j)
        #     if numbers[i] + numbers[j] == target:
        #         print("1st ",i,j)
        #         return [i+1,j+1]
        #     mid = (i + j) // 2
        #     # print("i",i)
        #     # print("j",j)
        #     # print(mid)
          
        #     if numbers[j] + numbers[i] > target:
        #         if numbers[mid] + numbers[i] <= target:
        #             j -= 1
        #         else:
        #             j = mid
        #     else:
        #         if numbers[mid] + numbers[j] <= target:
        #             i = mid
        #         else:
        #             i += 1


           
            

     
                
       
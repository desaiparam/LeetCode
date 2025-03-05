class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # se = set()
        # for i in nums:
        #     if i in se:
        #         return True
        #     se.add(i)
        # return False
        counter = set()
        for i in nums:
        # print(counter)
            if i not in counter:
                # counter(i) += 1
                counter.add(i)
            else:
                return True
        return False
            

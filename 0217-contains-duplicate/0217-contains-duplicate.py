class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                # seen[i] += 1
                return True
            # else:
        return False
            #     seen.add(i) = 1
        # print(seen >2)
        
        
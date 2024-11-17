class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            print("fewgrebg")
            return nums
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        d = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
        print(d)
        ans = []
        # for i , j in d.items():
        #     if j > k:
        #         ans.append(i)
        i = 0
        for j,key in d.items():
            if i < k:
                ans.append(j)
                i+=1
            else:
                break
        return ans

        
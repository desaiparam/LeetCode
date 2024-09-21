class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        q = len(arr)//4
        for i in range(len(arr)-q):
            if arr[i] == arr[i+q]:
                return arr[i]
        # return 1
        
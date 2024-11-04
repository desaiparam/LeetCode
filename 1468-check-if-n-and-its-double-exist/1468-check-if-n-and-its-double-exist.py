class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            d = arr[i] * 2
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) //2
                # print(arr[mid])
                if arr[mid] == d and mid != i:
                    return True
                elif arr[mid] < d:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


        
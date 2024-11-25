class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        ans = []
        
        while left < right:
            # if len(arr) == k:
            #     return ans
            mid = (left + right) // 2
            # if arr[mid] == x:
            #     ans.append(arr[mid])
            # elif arr[left] < x and arr[right] > x :
            #     # left += mid
            #     print(ans,arr[left])
            #     ans.append(arr[left])
            #     left += 1
            # elif arr[left] > x and arr[right] < x:
            #     print(ans,arr[right])
            #     ans.append(arr[right])
            #     right -= 1
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
            

        
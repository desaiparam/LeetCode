class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #Optimized O(N)
        count = 0
        window_sum = sum(arr[:k])
        if window_sum //k >= threshold:
            count += 1
        for i in range(k,len(arr)):
            window_sum = window_sum - arr[i-k] + arr[i]
            if window_sum //k >= threshold:
                count += 1

        #Brute Force O(n*k)
        # for i in range(len(arr)-k+1):
        #     current_sum = 0
        #     for j in range(k):
        #         current_sum = current_sum + arr[i+j]
        #         # print(current_sum)
        #     if current_sum//k >= threshold:
        #         # print()
        #         count+=1
        return count
                 
        
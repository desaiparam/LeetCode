class Solution {
    public int maxSubArray(int[] nums) {
        int n =nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        int result=dp[0];

        for(int i =1;i<n ;i++){
            dp[i] = Math.max(nums[i],dp[i-1]+nums[i]);
            result = Math.max(result,dp[i]);
            
        }
            System.out.print(result);
    return result;
    }
}
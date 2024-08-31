class Solution {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int result=dp[0];
        // dp[1] = Math.max(nums[1],dp[0]+nums[1]);
        for(int i =1;i<nums.length ;i++){
            dp[i] = Math.max(nums[i],dp[i-1]+nums[i]);
            result = Math.max(result,dp[i]);
            // temp[i] = dp[i];
            
        }
            System.out.print(result);
    return result;
    }
}
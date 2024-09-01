class Solution {
    public int lengthOfLIS(int[] nums) {
        int dp[] = new int[nums.length];
        dp[0] = 1;
        int result=0;
        for(int i=1;i<nums.length;i++){
        dp[i] = 1;
            for(int j=0;j<i;j++){
                if(nums[i] > nums[j]){
                dp[i] = Math.max(dp[i],dp[j]+1);
                // System.out.println("nums[j]"+nums[j]);
                }
            }
        }
        for(int i =0;i<dp.length;i++){
            result = Math.max(result,dp[i]);
        }
    return result;
    }
}
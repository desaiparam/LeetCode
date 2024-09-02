class Solution {
    public int findNumberOfLIS(int[] nums) {
        int dp[] = new int[nums.length];
        // dp[0] = 1;
        int count[] = new int[nums.length];
        int ans = 0, m=0;
        for (int i = 0; i < nums.length; i++) {
            // System.out.println("i++" + i);
            dp[i] = 1;
            count[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    // dp[i] = Math.max(dp[i], dp[j] + 1);
                    // count[i] = dp[j];
                    // if(dp[i]<d[j]+1)
                    if (dp[i] < dp[j] + 1) {
                        dp[i] = dp[j] + 1;
                        count[i] = count[j];
                    } else if (dp[i] == dp[j] + 1) {
                        count[i] += count[j];
                    }
                    // break;
                    // System.out.println("dp[i] after"+Math.max(dp[i],dp[j]+1));
                }
            }
                m=Math.max(m,dp[i]);
        }
            for(int i = 0 ;i<nums.length;i++){
                if(dp[i] == m){
                    ans+=count[i];
                }
            }
        return ans;
    }
}
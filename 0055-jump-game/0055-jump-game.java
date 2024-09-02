class Solution {
    public boolean canJump(int[] nums) {
        // boolean dp[] = new boolean[nums.length];
        // dp[0] = true;
        // for (int i = 1; i < nums.length; i++) {
        //     // dp[i] = false;
        //     for (int j = 0; j < i; j++) {
        //         if(j+nums[j] >= i &&dp[j]){
        //             // System.out.println("EWRTYh");
        //             dp[i] = true;
        //             break;
        //         } 
        //     }
        // }
        // return dp[nums.length - 1];

        int ans =0;
        for(int i =0;i<nums.length && i<=ans;i++){
            ans = Math.max(ans,Math.min(i+nums[i],nums.length-1));
        // System.out.println("ans"+i);
        }
        return ans == nums.length-1;
    }
}
// }

// if(nums.length==0){
// return false;
// }
// if(nums.length<=1){
// return true;
// }

// for(int i = 0;i<nums.length;i++){
// if(nums.length-1 == nums[i]+i){
// return true;
// }
// }

// return false;
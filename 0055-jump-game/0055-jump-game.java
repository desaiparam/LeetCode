class Solution {
    public boolean canJump(int[] nums) {
        int ans =0;
        for(int i =0;i<nums.length && i<=ans;i++){
            ans = Math.max(ans,Math.min(i+nums[i],nums.length-1));
        }
        return ans == nums.length-1;
    }
}
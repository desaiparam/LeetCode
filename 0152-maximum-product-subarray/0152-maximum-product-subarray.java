class Solution {
    public int maxProduct(int[] nums) {
        // int[] dp = new int[nums.length];
        // if(nums.length==0){
        // return 0;
        // }
        // int minP = nums[0];
        // int maxP = nums[0];
        // int result = maxP;
        // for(int i=1;i<nums.length;i++){
        // int temp = maxP;
        // maxP= Math.max(nums[i],Math.max(minP*nums[i],maxP*nums[i]));
        // minP = Math.min(nums[i],Math.max(temp*nums[i],minP*nums[i]));
        // result = Math.max(result,Math.max(minP,maxP));
        // }
        // return result;
        double pre = 1, suf = 1;
        double result  = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (pre == 0) {
                pre = 1;
            }
            if (suf == 0) {
                suf = 1;
            }
            pre *= nums[i];
            suf *= nums[nums.length -i- 1];
            result = Math.max(result, Math.max(pre, suf));
        }
        return (int)result;
    }
}
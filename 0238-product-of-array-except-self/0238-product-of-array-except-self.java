class Solution {
    public int[] productExceptSelf(int[] nums) {
        // int j = 0;
        int left[] = new int[nums.length];
        left[0] = 1;
        int right = 1;
        int[] ans = new int[nums.length];
        for (int i = 1; i < nums.length; i++) {
            left[i] = left[i - 1] * nums[i - 1];
            // System.out.println("left"+left[i]);
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            ans[i] = left[i] * right;
            right *= nums[i];
        }
        return ans;
    }
}
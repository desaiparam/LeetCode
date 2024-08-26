class Solution {
    public void moveZeroes(int[] nums) {
        int temp = 0;
        int i = 0;
        int j =0;
        while( j<nums.length){
            if(nums[j]!=0){
                temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                i++;
            }
                j++;
        }
        // for(int j=0;j<nums.length;j++){
        //     if(nums[j]!=0){
        //         temp = nums[j];
        //         nums[j] = nums[i];
        //         nums[i] = temp;
        //         i++;

        //     }
        
    }
}
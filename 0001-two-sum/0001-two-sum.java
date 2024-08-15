class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] totalNums = new int[2];
        for(int i =0;i<nums.length-1;i++){
            for(int j=i+1;j<nums.length;j++)
            if(nums[i]+nums[j]==target){
                // System.out.println(i); 
                totalNums[0] = i;
                totalNums[1] = j;
                return totalNums;
            }
//             else if(nums[i]+nums[i+2] == target){
//                 System.out.println(i+2);
//  totalNums[0] = i;
//                 totalNums[i++] = i+1;
//                 return totalNums;
//             }
        }
        return totalNums;
    }
}
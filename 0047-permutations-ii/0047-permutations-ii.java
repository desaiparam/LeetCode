class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> permuSet = new ArrayList<>();
        // List<List<Integer>> seenSeet = new ArrayList<>();
        Arrays.sort(nums);
        helper(nums,new ArrayList<>(),permuSet,new boolean[nums.length]);
        return permuSet;
    }

    public void helper(int[] nums, List<Integer> temp, List<List<Integer>> permuSet,boolean[] used) {
        if (temp.size() == nums.length) {
             permuSet.add(new ArrayList<>(temp));
        } else {
            for (int i = 0; i < nums.length; i++ ) {
                if(used[i] || i>0 && nums[i]==nums[i-1] && !used[i-1] ){
                    continue;
                }else{
                used[i] = true;
                temp.add(nums[i]);
                helper(nums,temp,permuSet,used);
                used[i] = false;
                temp.remove(temp.size()-1);
                }
            }
        }
    }
    
}
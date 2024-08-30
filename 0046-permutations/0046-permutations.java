class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> permuSet = new ArrayList<>();
        helper(nums,new ArrayList<>(),permuSet);
        return permuSet;
    }

    public void helper(int[] nums, List<Integer> temp, List<List<Integer>> permuSet) {
        if (temp.size() == nums.length) {
             permuSet.add(new ArrayList<>(temp));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if(temp.contains(nums[i])){
                    continue;
                }
                temp.add(nums[i]);
                helper(nums,temp,permuSet);
                temp.remove(temp.size()-1);
            }
        }
    }
}
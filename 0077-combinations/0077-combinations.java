class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> possCombi = new ArrayList<>(k);
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        helper(nums, new ArrayList<>(), possCombi, k, 0);
        return possCombi;
    }

    public void helper(int[] nums, List<Integer> temp, List<List<Integer>> possCombi, int k,int start) {
        if (temp.size() == k) {
            possCombi.add(new ArrayList<>(temp));
        } else {
            for (int i = start; i < nums.length; i++) {
                if (temp.contains(nums[i])) {
                    continue;
                } else {
                    temp.add(nums[i]);
                    helper(nums, temp, possCombi, k, i+1);
                    temp.remove(temp.size() - 1);

                }
            }
        }
    }
}
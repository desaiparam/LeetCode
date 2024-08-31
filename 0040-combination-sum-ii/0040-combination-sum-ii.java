class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> subSet = new ArrayList<>();
        helper(candidates, target, subSet, new ArrayList<>(), 0);
        return subSet;
    }

    public void helper(int[] candidates, int target, List<List<Integer>> subSet, List<Integer> temp, int start) {
        Arrays.sort(candidates);
        if (target == 0) {
            subSet.add(new ArrayList<>(temp));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > target) {
                continue;
            }
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            temp.add(candidates[i]);
            helper(candidates, target - candidates[i], subSet, temp, i + 1);
            temp.remove(temp.size() - 1);
        }
    }
}
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> subSet = new ArrayList<>();
        helper(candidates, target, subSet, new ArrayList<>(), 0);
        return subSet;
    }

    public void helper(int[] candidates, int target, List<List<Integer>> subSet, List<Integer> temp, int start) {
        if (target==0) {
            subSet.add(new ArrayList<>(temp));
            // return;
        }
        for (int i = start; i < candidates.length;i++) {
            // if(temp!=target){
                if(candidates[i]>target){
                continue;
                }
            temp.add(candidates[i]);
            helper(candidates, target-candidates[i], subSet, temp, i);
            // }
            temp.remove(temp.size() - 1);
        }
    }
}
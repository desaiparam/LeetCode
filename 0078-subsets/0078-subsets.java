class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        subsets.add(new ArrayList<>());
        for (int i : nums) {
           List<List<Integer>> tempSubsets = new ArrayList<>();
            for (List<Integer> subset : subsets) {
                 List<Integer> newTempSubsets = new ArrayList<>(subset);
                // temp=;
                newTempSubsets.add(i);
                tempSubsets.add(newTempSubsets);
            }
            subsets.addAll(tempSubsets);
        }
        return subsets;
    }
}
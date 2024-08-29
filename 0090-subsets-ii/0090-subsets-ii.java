class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        Set<List<Integer>> seenSubsets = new HashSet<>();
        subsets.add(new ArrayList<>());
        seenSubsets.add(new ArrayList<>());
 Arrays.sort(nums);
        for (int i : nums) {
            List<List<Integer>> tempSubsets = new ArrayList<>();
            for (List<Integer> subset : subsets) {
                List<Integer> newTempSubsets = new ArrayList<>(subset);
                // temp=;
                newTempSubsets.add(i);
                if (!seenSubsets.contains(newTempSubsets)) {
                    seenSubsets.add(newTempSubsets);
                    tempSubsets.add(newTempSubsets);
                }
            }
            subsets.addAll(tempSubsets);
        }
        return subsets;
    }
}
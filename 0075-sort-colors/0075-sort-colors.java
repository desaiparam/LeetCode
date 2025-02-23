class Solution {
    public void sortColors(int[] nums) {
        Map<Integer,Integer> map = new HashMap();
        map.put(0,0);
        map.put(1,0);
        map.put(2,0);
        for (int i:nums){
            map.put(i,map.get(i) + 1);
        }
        // System.out.print(map);
        int index = 0;
        for(int c =0;c <3;c++){
            int f = map.get(c);
            for(int j =0;j<f;j++){
                nums[index] = c;
                index++;
            }
        }
    }
}
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] inD = new int[numCourses];
        helper(inD, prerequisites);
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < inD.length; i++) {
            if (inD[i] == 0) {
                q.add(i);
            }
        }
        List<Integer> res = new ArrayList<>();
        while (!q.isEmpty()) {
            int curr = q.poll();
            res.add(curr);
            for (int i = 0; i < prerequisites.length; i++) {
                if (prerequisites[i][1] == curr) {
                    inD[prerequisites[i][0]]--;
                    if (inD[prerequisites[i][0]] == 0) {
                        q.add(prerequisites[i][0]);
                    }
                }
            }
        }
        if (res.size() != numCourses) {
            return new int[0];
        }
        int[] finRes = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            finRes[i] = res.get(i);
        }
        return finRes;
    }

    public void helper(int[] inD, int[][] prerequisites) {
        for (int i = 0; i < prerequisites.length; i++) {
            inD[prerequisites[i][0]]++;
        }
    }
}
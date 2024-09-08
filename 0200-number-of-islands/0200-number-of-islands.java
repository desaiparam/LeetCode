class Solution {
    List<Integer> rank = new ArrayList<>();
    List<Integer> parent = new ArrayList<>();
    int count = 0;

    public void disJoint(int n,int m) {
        for (int i = 0; i < n*m; i++) {
            parent.add(i);
            rank.add(0);
        }
    }

    public int findUPar(int node) {
        if (node == parent.get(node)) {
            return node;
        }
        int ulp = findUPar(parent.get(node));
        parent.set(node, ulp);
        return parent.get(node);
    }

    public void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) {
            return;
        }
        if (rank.get(ulp_u) < rank.get(ulp_v)) {
            parent.set(ulp_u, ulp_v);
        } else if (rank.get(ulp_u) > rank.get(ulp_v)) {
            parent.set(ulp_v, ulp_u);
        } else {
            parent.set(ulp_v, ulp_u);
            int rankU = rank.get(ulp_u);
            rank.set(ulp_u, rankU + 1);
        }
            count-=1;
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int n = grid.length;
        int m = grid[0].length;
        disJoint(n, m);
        for(int i =0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]=='1'){
                    count+=1;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    // int node = i * m + j
                    grid[i][j] = '0';
                    if (i - 1 >= 0 && grid[i - 1][j] == '1') {
                        unionByRank(i * m + j, (i - 1) * m + j);
                    }
                    if (i + 1 < n && grid[i + 1][j] == '1') {
                        unionByRank(i * m + j, (i + 1) * m + j);
                    }
                    if (j - 1 >= 0 && grid[i][j - 1] == '1') {
                        unionByRank(i * m + j, i * m + j - 1);
                    }
                    if (j + 1 < m && grid[i][j + 1] == '1') {
                        unionByRank(i * m + j, i * m + j + 1);
                    }
                }

            }
        }
        // int count = 0;
        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < m; j++) {
        //         if (grid[i][j] == '0') {
        //             int node = i * m + j;
        //             if (findUPar(node) == node) {
        //                 count++;
        //             }
        //         }
        //     }
        // }
        return count;
    }
}
class Solution {
    List<Integer> rank = new ArrayList<>();
    List<Integer> parent = new ArrayList<>();

    public void disJoint(int n) {
        for (int i = 0; i <= n; i++) {
            rank.add(0);
            parent.add(i);
        }
    }

    public int findUpar(int node) {
        if (node == parent.get(node)) {
            return node;
        }
        int ulp = findUpar(parent.get(node));
        parent.set(node, ulp);
        return parent.get(node);
    }

    public void unionByRank(int u, int v) {
        int ulp_u = findUpar(u);
        int ulp_v = findUpar(v);
        if (ulp_u == ulp_v) {
            return;
        }
        if (rank.get(ulp_u) < rank.get(ulp_v)) {
            parent.set(ulp_u, ulp_v);
        }
        else if (rank.get(ulp_v) < rank.get(ulp_u)) {
            parent.set(ulp_v, ulp_u);
        } else {
            parent.set(ulp_v, ulp_u);
            int rankU = rank.get(ulp_u);
            rank.set(ulp_u, rankU + 1);
        }
    }

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        //  for (int i = 0; i <= n; i++) {
        //     rank.add(0);
        //     parent.add(i);
        // }
        disJoint(n);
        // for(int i=0;i<edges.length;i++){
        // for(int j=0;j<edges[i].length;j++){
        // unionByRank(edges[i][0],edges[0][j]);
        // }
        // }
        for (int i = 0; i < edges.length; i++) {
            unionByRank(edges[i][0], edges[i][1]);
        }
        return valid(source, destination);
    }

    public boolean valid(int source, int destination) {
        if (findUpar(source) == findUpar(destination)) {
            return true;
        }
        return false;
    }
}
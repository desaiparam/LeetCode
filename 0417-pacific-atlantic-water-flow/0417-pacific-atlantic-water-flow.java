class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int row = heights.length;
        int col = heights[0].length;
        if(row==0||col==0){
            return res;
        }
        boolean[][] ao = new boolean[row][col];
        boolean[][] po = new boolean[row][col];
        for(int i =0;i<col;i++){
            dfs(0,i,po,heights[0][i],heights);
            dfs(row-1,i,ao,heights[row-1][i],heights);
        }
        for(int j=0;j<row;j++){
            dfs(j,0,po,heights[j][0],heights);
            dfs(j,col-1,ao,heights[j][col-1],heights);
        }
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(po[i][j] && ao[i][j]){
                    List<Integer> temp = new ArrayList<>();
                    temp.add(i);
                    temp.add(j);
                    res.add(temp);
                }
            }
        }
        return res;
    }
    public void dfs(int r , int c , boolean [][] visited , int h , int[][]heights){
        if(r<0||c<0||r==heights.length||c==heights[0].length|| visited[r][c] || h>heights[r][c]){
            return;
        }
        visited[r][c] =true;
        dfs(r+1,c,visited,heights[r][c],heights);
        dfs(r,c+1,visited,heights[r][c],heights);
        dfs(r-1,c,visited,heights[r][c],heights);
        dfs(r,c-1,visited,heights[r][c],heights);
    }
}
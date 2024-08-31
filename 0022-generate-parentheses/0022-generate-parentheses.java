class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> combi = new ArrayList<>();
        helper(n, new StringBuilder(), combi,0,0);
        return combi;
    }
    public void helper(int n , StringBuilder temp,List<String> combi,int openBrack,int closeBrack){
        if(temp.length() == (n*2)){
           combi.add(temp.toString());
            return ;
        }
            if(openBrack<n){
            temp.append("(");
            System.out.println(openBrack);
            helper(n,temp,combi,openBrack+1,closeBrack);
            temp.deleteCharAt(temp.length() - 1);
            }
            if(closeBrack<openBrack){
                temp.append(")");
                helper(n,temp,combi,openBrack,closeBrack+1);
                temp.deleteCharAt(temp.length() - 1);
            }
    }
}
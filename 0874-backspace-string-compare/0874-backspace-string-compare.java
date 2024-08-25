class Solution {
    public boolean backspaceCompare(String s, String t) {
        return helper(s).equals(helper(t));
    }
    public String helper(String s){
        StringBuilder newS = new StringBuilder();
        char[] cha = s.toCharArray();
         for (int i = 0; i < cha.length; i++) {
            if (cha[i] == '#' && newS.length()!=0) {
                // newS.deleteCharAt(i);
                newS.deleteCharAt(newS.length() - 1);
                continue;
            }
            if(cha[i]!= '#'){
                newS.append(cha[i]);
            }
            // if(ch[i] !='#'){
            //     newS.append
            // }
        }
        //  System.out.println("newS" + newS);
         return newS.toString();
    }
}
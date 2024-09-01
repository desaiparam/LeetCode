class Solution {
    public String longestPalindrome(String s) {
       if(s=="" || s.length()<1){
        return "";
       }
       int st = 0,e=0;
       for(int i =0;i<s.length();i++){
        int len1 = helper(s,i,i);
        int len2 = helper(s,i,i+1);
        int len = Math.max(len1,len2);
        if(len>e -st){
            st = i-(len -1)/2;
            e = i+len/2;
        }
       }
       return s.substring(st,e+1);
    }
    public int helper(String s , int i ,int j){
        while(i>=0 && j<s.length() && s.charAt(i)==s.charAt(j)){
            i--;
            j++;
        }
        return j-i-1;
    }

}
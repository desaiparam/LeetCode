import java.util.*;

class Solution {
    public int romanToInt(String s) {

        Hashtable<Character, Integer> hashtable = new Hashtable<Character, Integer>();
        hashtable.put('I', 1);
        hashtable.put('V', 5);
        hashtable.put('X', 10);
        hashtable.put('L', 50);
        hashtable.put('C', 100);
        hashtable.put('D', 500);
        hashtable.put('M', 1000);
        // char[] c = new char[s.length()];
        int sol = 0;
        for (int i = 0; i < s.length(); i++) {
            // c[i] = s.charAt(i);
            // System.out.print(c[i]);
            // sol+=hashtable.get(s.charAt(i));
            if (i < s.length() - 1 && hashtable.get(s.charAt(i)) < hashtable.get(s.charAt(i + 1))) {
                sol -= hashtable.get(s.charAt(i));
            } else {
                sol += hashtable.get(s.charAt(i));
            }
            // if(s.length()>0 && s.charAt(i)=='V'&& s.charAt(i-1)=='I'){
            // sol=sol-1;
            // }
            // else if(s.length()>0 &&s.charAt(i)=='X' && s.charAt(i-1)=='I'){
            // sol=sol-1;
            // }
            // else if(s.length()>0 &&s.charAt(i)=='L' && s.charAt(i-1)=='X' ){
            // sol=sol-10;
            // }
            // else if(s.length()>0 &&s.charAt(i)=='C'&&s.charAt(i-1)=='X'){
            // sol=sol-10;
            // }
            // else if(s.length()>0 &&s.charAt(i)=='D'&&s.charAt(i-1)=='C'){
            // sol=sol-100;
            // }
            // else if( s.length()>0 && s.charAt(i)=='M'&&s.charAt(i-1)=='C'){
            // sol=sol-100;
            // }

            System.out.print(sol);

        }
        System.out.print(hashtable);

        return sol;
    }
}
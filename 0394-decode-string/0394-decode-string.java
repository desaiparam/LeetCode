import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public String decodeString(String s) {
        Stack<Integer> intg = new Stack<>();
        Stack<StringBuilder> str = new Stack<>();
        StringBuilder sb1 = new StringBuilder();
        int n= 0;
        for(char c: s.toCharArray()){
            if(Character.isDigit(c)){
                n = n*10+(c-'0');
            }else if(c=='['){
                intg.push(n);
                n=0;
                str.push(sb1);
                sb1=new StringBuilder();
            }else if(c==']'){
                int k = intg.pop();
                StringBuilder temp =sb1;
                sb1= str.pop();
                while(k-- >0){
                    sb1.append(temp);
                }
            }else{
                sb1.append(c);
            }
        } 
return sb1.toString();
    }
}
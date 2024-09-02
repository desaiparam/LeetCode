import java.util.HashMap;

class Solution {
    public int numDecodings(String s) {
        HashMap<String, String> decode = new HashMap<String, String>();
        decode.put("1", "A");
        decode.put("2", "B");
        decode.put("3", "C");
        decode.put("4", "D");
        decode.put("5", "E");
        decode.put("6", "F");
        decode.put("7", "G");
        decode.put("8", "H");
        decode.put("9", "I");
        decode.put("10", "J");
        decode.put("11", "K");
        decode.put("12", "L");
        decode.put("13", "M");
        decode.put("14", "N");
        decode.put("15", "O");
        decode.put("16", "P");
        decode.put("17", "Q");
        decode.put("18", "R");
        decode.put("19", "S");
        decode.put("20", "T");
        decode.put("21", "U");
        decode.put("22", "V");
        decode.put("23", "W");
        decode.put("24", "X");
        decode.put("25", "Y");
        decode.put("26", "Z");
        int dp[] = new int[s.length()+1];
        dp[0] = 1;
        for (int i = 1; i <= s.length(); i++) {
            String onD = s.substring(i - 1, i);
            if (decode.containsKey(onD)) {
                dp[i] += dp[i - 1];
            }
            if(i>1){
            String twoD =s.substring(i - 2, i );
                if(decode.containsKey(twoD)){
                    dp[i] += dp[i-2];
                }
            }
        }
        return dp[s.length()];
    }

}
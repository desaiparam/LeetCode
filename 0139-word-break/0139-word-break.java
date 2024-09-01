class Solution {
    static class Node {
        Node children[];
        boolean eod;

        public Node() {
            this.children = new Node[26];
            this.eod = false;
        }
    }

    public void insert(Node head, String str) {
        Node temp = head;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (temp.children[ch - 'a'] == null) {
                temp.children[ch - 'a'] = new Node();
            }
            // temp.children[ch - 'a'].count++;
            temp = temp.children[ch - 'a'];
        }
        temp.eod = true;
    }

    public boolean checkWord(Node head, String str) {
        int n = str.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 0; i < n; i++) {
            if (!dp[i]) {
            continue;
            }
            Node temp = head;
            for (int j = i ; j<n; j++) {
                char ch = str.charAt(j);
                if (temp.children[ch - 'a'] == null) {
                    break;
                }
                temp = temp.children[ch - 'a'];
                if (temp.eod) {
                    dp[j+1] = true;
                    // break;
                }
            }
        }
        return dp[n];
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        Node head = new Node();
        for (int i = 0; i < wordDict.size(); i++) {
            insert(head, wordDict.get(i));
        }
        return checkWord(head, s);
    }
}
class Solution {
    static class Node{
        Node children[] = new Node[26];
        int count;
        public Node(){
            this.children = new Node[26];
            this.count = 0;
        }
    }
    public void insert(Node head,String str){
        Node temp=head;
        for(int i=0;i<str.length();i++){
            char ch= str.charAt(i);
            if(temp.children[ch-'a'] == null){
                temp.children[ch-'a'] = new Node();
            }
            temp.children[ch-'a'].count++;
            temp=temp.children[ch-'a'];
        }
    }
    public String prefix(Node head,String str ,int n){
        System.out.println(str);
        Node temp = head;
        for(int i=0;i<str.length();i++){
            char ch = str.charAt(i);
            if(temp.children[ch-'a'].count<n && i == 0){
return "";
            }
            if(temp.children[ch-'a'].count<n&&i>0){
                return str.substring(0,i);
            }
            temp = temp.children[ch-'a'];
        }
        return str;
    }
    public String longestCommonPrefix(String[] strs) {
        String sol= "";
        if(strs.length==1){
            return strs[0];
        }
        Node head = new Node();
        for (int i =0;i<strs.length;i++){
            insert(head,strs[i]);
        }
        String prefix = prefix(head,strs[0],strs.length);
        if(prefix.length()>sol.length()){
            sol=prefix;
        }
        return sol;
    }
}
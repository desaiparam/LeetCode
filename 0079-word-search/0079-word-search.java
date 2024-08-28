class Solution {
    public boolean exist(char[][] board, String word) {
        // char[] arr = word.toCharArray();
        // f÷or(int j=0;j<arr.length;j++){
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (helper(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean helper(char[][] board, int i, int j, String word, int index) {

        if (index == word.length()) {
            return true;
        }
        if (i < 0 || i >= board.length || j < 0 || j >= board[i].length || board[i][j] != word.charAt(index)) {
            return false;
        }
        char temp = board[i][j];
        board[i][j]='*';

        boolean found = helper(board, i + 1, j, word, index + 1) ||
                helper(board, i - 1, j, word, index + 1) ||
                helper(board, i, j + 1, word, index + 1) ||
                helper(board, i, j - 1, word, index + 1);
            //         System.out.println(word);
            // return true;
        board[i][j]=temp;
        return found;
    }
}
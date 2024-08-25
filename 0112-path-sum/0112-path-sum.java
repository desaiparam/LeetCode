/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        // TreeNode curr = root;
        // // int sum = 0;
        // // System.out.print(sum);
        // // if(sum==targetSum){
        // // return true;
        // // }
        // if(targetSum==0){
        // return true;
        // }
        // while (curr.left != null && curr.right!=null) {
        // // System.out.print(" " + curr.val);
        // // if (sum!=targetSum){

        // hasPathSum(curr.left,targetSum-=curr.left.val);
        // hasPathSum(curr.right,targetSum-=curr.right.val);
        // // }
        // }
        // return false;

        TreeNode curr = root;
        if (curr == null) {
            return false;
        }
        targetSum -= curr.val;
        if (curr.left == null && curr.right == null) {
            return targetSum == 0;
        }

        return hasPathSum(curr.left, targetSum) || hasPathSum(curr.right, targetSum);

    }
}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode reverse = null; 
        while (current!= null){
            ListNode newNode = current.next;
        current.next=reverse;
        reverse = current;
        current = newNode;
        System.out.print(reverse.val);

        }
        // System.out.print(head.next); 
    return reverse;
    }
}
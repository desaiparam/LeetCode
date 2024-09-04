/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
     if(head==null||head.next==null){
        return head;
     }
     ListNode midd = getMidd(head);
     ListNode nmidd = midd.next;
     midd.next= null;
    ListNode left = sortList(head);
    ListNode right = sortList(nmidd);
    ListNode sortedL= merge(left,right);
    return sortedL;
    }

    public ListNode merge(ListNode left, ListNode right) {
        ListNode res = null;
        if (left == null) {
            return right;
        }
        if (right == null) {
            return left;
        }
        if (left.val < right.val) {
            res = left;
            res.next = merge(left.next, right);
        } else {
            res = right;
            res.next = merge(left, right.next);
        }
        return res;
    }

    public ListNode getMidd(ListNode m) {
        if (m == null) {
            return m;
        }
        ListNode slow = m, fast = m;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
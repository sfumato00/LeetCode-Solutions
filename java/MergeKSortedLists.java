public class MergeKSortedLists {

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

        private ListNode[] _lists;

        public ListNode mergeKLists(ListNode[] lists) {
            if (lists == null || lists.length == 0) {
                return null;
            }
            _lists = lists;
            mergeKLists(0, lists.length);
            return _lists[0];
        }

        private void mergeKLists(int lo, int hi) {
            if (lo + 1 >= hi) {
                return;
            }

            int mid = lo + (hi - lo) / 2;
            mergeKLists(lo, mid);
            mergeKLists(mid, hi);
            _lists[lo] = merge(_lists[lo], _lists[mid]);
        }

        private ListNode merge(ListNode head1, ListNode head2) {
            var dummy = new ListNode();
            var prev = dummy;
            var p1 = head1;
            var p2 = head2;

            while (p1 != null && p2 != null) {
                if (p1.val <= p2.val) {
                    prev.next = p1;
                    p1 = p1.next;
                } else {
                    prev.next = p2;
                    p2 = p2.next;
                }
                prev = prev.next;
            }

            prev.next = p1 != null ? p1 : p2;
            return dummy.next;
        }
    }
}
from ast import List
import heapq
from typing import Optional

from commons import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # return self.mergeKLists_heap(lists)
        return self.mergeKLists_divide_and_conquer(lists)

    def mergeKLists_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        head = ListNode()
        prev = head

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(hp, (node.val, i, node))

        while hp:
            _, index, node = heapq.heappop(hp)
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(hp, (node.next.val, index, node.next))
        return head.next

    def mergeKLists_divide_and_conquer(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        def merge(lst1, lst2):
            return merge_iteration(lst1, lst2)

        def merge_iteration(lst1, lst2):
            head = ListNode()
            prev = head
            while lst1 and lst2:
                if lst1.val <= lst2.val:
                    prev.next = lst1
                    lst1 = lst1.next
                    prev = prev.next
                else:
                    prev.next = lst2
                    lst2 = lst2.next
                    prev = prev.next
            prev.next = lst1 if lst1 else lst2
            return head.next

        def merge_recursion(lst1, lst2):
            if not lst1 and not lst2:
                return None
            if not lst1:
                return lst2
            if not lst2:
                return lst1

            if lst1.val <= lst2.val:
                lst1.next = merge(lst1.next, lst2)
                return lst1
            else:
                lst2.next = merge(lst1, lst2.next)
                return lst2

        def merge_lists(lists, lo, hi):
            if lo + 1 >= hi:  # [lo, hi)
                return
            mid = lo + (hi - lo) // 2
            merge_lists(lists, lo, mid)
            merge_lists(lists, mid, hi)
            lists[lo] = merge(lists[lo], lists[mid])

        merge_lists(lists, 0, len(lists))
        return lists[0]

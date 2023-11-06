from typing import List


class Solution:
    def intervalIntersection(
        self, list1: List[List[int]], list2: List[List[int]]
    ) -> List[List[int]]:
        m, n = len(list1), len(list2)
        i, j = 0, 0
        out = []
        while i < m and j < n:
            start, end = max(list1[i][0], list2[j][0]), min(list1[i][1], list2[j][1])

            if start <= end:
                out += [[start, end]]

            if list1[i][1] <= list2[j][1]:
                i += 1
            else:
                j += 1

        return out

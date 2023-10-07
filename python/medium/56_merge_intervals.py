from typing import List


class Solution:
    """Time: O(NLogN), Space: O(1)"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        prev, last = n - 1, n - 1

        for i in range(n - 2, -1, -1):
            if intervals[prev][0] <= intervals[i][1]:
                intervals[i][:] = (
                    min(intervals[prev][0], intervals[i][0]),
                    intervals[prev][1],
                )
                intervals[prev][:] = intervals[last]
                last -= 1
                intervals.pop()
            prev = i

        intervals.sort()
        return intervals

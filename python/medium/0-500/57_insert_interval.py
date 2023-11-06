class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        out = []
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                return out + [newInterval] + intervals[i:]

            if max(newInterval[0], interval[0]) <= min(newInterval[1], interval[1]):
                newInterval[0], newInterval[1] = min(newInterval[0], interval[0]), max(
                    newInterval[1], interval[1]
                )
            else:
                out.append(interval)
        return out + [newInterval]

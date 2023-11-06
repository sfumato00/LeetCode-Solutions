class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        count = 0
        for s, e in intervals[1:]:
            if prev_end <= s:
                prev_end = e
            else:
                prev_end = min(e, prev_end)
                count += 1
        return count

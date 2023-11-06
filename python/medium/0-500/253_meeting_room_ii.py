class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        events = []
        for i in intervals:
            events += [(i.start, 1)]
            events += [(i.end, -1)]

        events.sort()

        max_count = 0
        count = 0
        for _, e in events:
            count += e
            max_count = max(max_count, count)
        return max_count

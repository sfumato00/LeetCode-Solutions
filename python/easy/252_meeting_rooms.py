class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        # Write your code here
        if not intervals:
            return True
        intervals.sort()

        end = intervals[0][1]
        for s, e in intervals[1:]:
            if end > s:
                return False
            end = e
        return True

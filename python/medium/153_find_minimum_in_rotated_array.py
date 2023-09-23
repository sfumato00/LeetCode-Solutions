from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Eliminate an edge case where nums is non-decreasing.
        if nums[-1] > nums[0]:
            return nums[0]
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # Since we eliminate the non-rotation case, we only need to consider rotation case.
            # Hence, if the mid value is large or equal to the first value, the minimum value must be either: right to the mid point or the first value.
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid
        # taken into an account of the edge case where nums has single value, e.g. [1] or [1,1]
        return nums[0] if lo == n else nums[lo]

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            m = lo + (hi - lo) // 2
            if nums[m] == target:
                return m

            if (
                nums[lo] <= nums[m] < target
                or target < nums[lo] <= nums[m]
                or nums[m] < target < nums[lo]
            ):
                lo = m + 1
            else:
                hi = m

        return -1

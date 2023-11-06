from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if (
                mid == 0
                and nums[mid] > nums[mid + 1]
                or mid == n - 1
                and nums[mid - 1] < nums[mid]
                or nums[mid - 1] < nums[mid] > nums[mid + 1]
            ):
                return mid
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

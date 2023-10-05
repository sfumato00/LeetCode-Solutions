class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2

            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        if lo == n or nums[lo] != target:
            return [-1, -1]

        start = lo

        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1

        return [start, lo - 1]

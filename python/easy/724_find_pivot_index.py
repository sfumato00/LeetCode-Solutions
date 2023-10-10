class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = sum(nums)
        curr = 0
        for i, x in enumerate(nums):
            curr += x
            if _sum - curr + x == curr:
                return i
        return -1

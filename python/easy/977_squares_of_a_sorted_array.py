class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        output = []
        while lo <= hi:
            if abs(nums[lo]) >= nums[hi]:
                output.append(nums[lo] ** 2)
                lo += 1
            else:
                output.append(nums[hi] ** 2)
                hi -= 1
        return output[::-1]

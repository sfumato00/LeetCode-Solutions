class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # lo, hi = 0, len(nums) - 1
        # while lo < hi:

        #     while lo < hi and nums[lo] % 2 == 0:
        #         lo += 1

        #     while lo < hi and nums[hi] % 2 == 1:
        #         hi -= 1

        #     if lo < hi:
        #         nums[lo], nums[hi] = nums[hi], nums[lo]

        # return nums

        j = 0
        for i, x in enumerate(nums):
            if x % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

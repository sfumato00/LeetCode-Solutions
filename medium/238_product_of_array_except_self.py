from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        def single_pass():
            pre, post = 1, 1
            for i in range(n):
                ans[i] *= pre
                pre *= nums[i]
                ans[n - i - 1] *= post
                post *= nums[n - i - 1]
            return ans

        def two_pass():
            pre, post = 1, 1
            for i, x in enumerate(nums):
                ans[i] *= pre
                pre *= x
            for i, x in enumerate(nums[::-1]):
                ans[n - 1 - i] *= post
                post *= x
            return ans

        return two_pass()

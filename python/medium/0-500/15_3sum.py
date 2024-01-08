from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i, x in enumerate(nums[:-2]):
            if x > 0:
                break

            if i > 0 and x == nums[i - 1]:
                continue

            t, lo, hi = -x, i + 1, n - 1
            while lo < hi:
                if (s := nums[lo] + nums[hi]) == t:
                    ans += [[x, nums[lo], nums[hi]]]
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

                elif s < t:
                    lo += 1
                else:
                    hi -= 1

        return ans

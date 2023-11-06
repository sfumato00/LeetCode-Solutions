from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for x in range(n - 2):
            if nums[x] > 0:
                break
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            y, z = x + 1, n - 1
            target = -nums[x]
            while y < z:
                _sum = nums[y] + nums[z]
                if _sum == target:
                    ans += [[nums[x], nums[y], nums[z]]]

                    y += 1
                    z -= 1
                    while y < z and nums[y] == nums[y - 1]:
                        y += 1
                    while y < z and nums[z] == nums[z + 1]:
                        z -= 1
                    continue
                elif _sum < target:
                    y += 1
                else:
                    z -= 1
        return ans

from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        nums = [0] * 121
        for x in ages:
            nums[x] += 1

        # calculate the prefix sum
        for i in range(121):
            nums[i] += nums[i - 1]

        out = 0
        for x in ages:
            # age lower than 14 will contradict rule #1 and #2
            if x <= 14:
                continue
            low = x // 2 + 7
            out += nums[x] - nums[low] - 1
        return out

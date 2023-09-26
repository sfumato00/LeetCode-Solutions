from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # left, right = [0] * n, [0] * n
        # from_left, from_right = 0, 0
        # for i in range(n):
        #     from_left = max(from_left, height[i])
        #     from_right = max(from_right, height[n - i - 1])
        #     left[i] = from_left
        #     right[n - i - 1] = from_right
        # ans = 0
        # for i, h in enumerate(height):
        #     ans += min(left[i], right[i]) - h
        # return ans

        lo, hi = 0, n - 1
        ans = 0
        left_max, right_max = height[0], height[n - 1]
        while lo < hi:
            if left_max <= right_max:
                lo += 1
                left_max = max(left_max, height[lo])
                ans += left_max - height[lo]
            else:
                hi -= 1
                right_max = max(right_max, height[hi])
                ans += right_max - height[hi]
        return ans

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        out = []
        for i, x in enumerate(nums):
            if q and i - q[0] >= k:
                q.popleft()

            while q and x > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i + 1 >= k:
                out += [nums[q[0]]]
        return out

from collections import defaultdict
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.data = defaultdict(list)
        for i, x in enumerate(nums):
            self.data[x] += [i]

    def pick(self, target: int) -> int:
        arr = self.data[target]
        n = len(arr)
        return arr[0] if n == 1 else arr[random.randrange(0, len(arr), 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

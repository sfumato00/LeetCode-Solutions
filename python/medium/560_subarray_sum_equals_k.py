from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int, {0: 1})
        ans, _sum = 0, 0
        for x in nums:
            _sum += x
            ans += sums[_sum - k]
            sums[_sum] += 1
        return ans

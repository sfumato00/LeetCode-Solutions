from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer–Moore majority
        memo = {}
        for x in nums:
            if x in memo or len(memo) < 3:
                memo[x] = memo.get(x, 0) + 1
            else:
                to_delete = [k for k, v in memo.items() if v == 1]
                for k in to_delete:
                    memo.pop(k)
                for k in memo:
                    memo[k] -= 1
                memo[x] = 1
        th = len(nums) // 3
        for k in memo:
            memo[k] = 0
        for x in nums:
            if x in memo:
                memo[x] += 1
        return [k for k, v in memo.items() if v > th]

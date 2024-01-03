from typing import List


class Solution:
    # def reductionOperations(self, nums: List[int]) -> int:
    #     # bruteforce
    #     ans = 0
        
    #     values = defaultdict(int)
    #     max_hp = []
    #     for i, x in enumerate(nums):
    #         values[x] += 1

    #     for k, v in values.items():
    #         heapq.heappush(max_hp, (-k, v))
        
    #     while len(max_hp) > 1:
    #         largest, next_largest = heapq.heappop(max_hp), heapq.heappop(max_hp)
    #         ans += largest[1]
    #         heapq.heappush(max_hp, (next_largest[0], next_largest[1] + cnt))

    #     return ans

    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort(reverse=True) # possibly improved by bucket sort
        # nums = self.bucketsort(nums)
        ans, curr = 0, 0
        prev = nums[0]
        for x in nums:
            if x != prev:
                ans += curr
            curr += 1
            prev = x
        return ans

    def bucketsort(self, nums: List[int]) -> int:

        MAX_VAL = 50_001
        bucket = [0] * MAX_VAL

        for x in nums:
            bucket[x] += 1
        output = []
        for v in range(MAX_VAL - 1, 0, -1):
            if bucket[v] > 0:
                output += [v] * bucket[v]

        return output
        


    
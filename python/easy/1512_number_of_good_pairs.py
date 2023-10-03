class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([x * (x - 1) // 2 for x in Counter(nums).values() if x > 1])

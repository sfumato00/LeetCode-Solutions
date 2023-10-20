class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _sum = 0
        _max = 0
        for x in nums:
            _sum += x
            _max = max(_max, x)
        _sum2 = 0
        for i in range(_max + 1):
            _sum2 += i
        return _max + 1 if _max < len(nums) else _sum2 - _sum

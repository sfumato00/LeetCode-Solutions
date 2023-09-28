class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # (a + n * k) % d = a % d
        mem = {0: -1}
        prefix_sum = 0

        for i, x in enumerate(nums):
            prefix_sum += x
            prefix_sum %= k
            if prefix_sum in mem:
                if i - mem[prefix_sum] > 1:
                    return True
            else:
                mem[prefix_sum] = i
        return False

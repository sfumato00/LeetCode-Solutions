class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            curr, d = 0, 1
            for x in weights:
                if curr + x > mid:
                    d += 1
                    curr = 0
                curr += x
            if d > days:
                lo = mid + 1
            else:
                hi = mid
        return lo

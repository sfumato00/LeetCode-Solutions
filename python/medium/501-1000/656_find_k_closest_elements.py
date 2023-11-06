class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x <= arr[mid] or x - arr[mid] <= arr[mid + k] - x:
                hi = mid
            else:
                lo = mid + 1

        return arr[lo : lo + k]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        lo, hi = 0, n - 1

        while hi - lo + 1 > k:
            if arr[hi] - x >= x - arr[lo]:
                hi -= 1
            else:
                lo += 1

        return arr[lo : hi + 1]


class Solution3:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hp = []

        for y in arr:
            heapq.heappush(hp, (abs(y - x), y))

        out = []
        for i in range(k):
            _, y = heapq.heappop(hp)
            out.append(y)
        return sorted(out)

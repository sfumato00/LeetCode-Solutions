class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counter = Counter(nums)

        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            cnt1, cnt2 = 1 + heapq.heappop(max_heap), 1 + heapq.heappop(max_heap)
            if cnt1 < 0:
                heapq.heappush(max_heap, cnt1)
            if cnt2 < 0:
                heapq.heappush(max_heap, cnt2)
        return -max_heap[0] if max_heap else 0

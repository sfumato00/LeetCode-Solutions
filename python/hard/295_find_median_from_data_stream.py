import heapq


class MedianFinder:
    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.right, num)
        elif self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        elif self.left and num < -self.left[0]:
            heapq.heappush(self.left, -num)
        elif len(self.left) < len(self.right):
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        while len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

        while len(self.left) > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        return (
            self.right[0]
            if len(self.right) > len(self.left)
            else (self.right[0] - self.left[0]) / 2
        )


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# left: [-1]
# right: [2,3]

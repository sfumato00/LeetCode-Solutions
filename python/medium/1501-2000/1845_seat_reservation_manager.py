class SeatManager:
    def __init__(self, n: int):
        self.hp = []
        self.idx = 0
        self.n = n

    def reserve(self) -> int:
        if self.hp:
            return heapq.heappop(self.hp)

        self.idx += 1
        return self.idx

    def unreserve(self, seatNumber: int) -> None:
        if 1 <= seatNumber <= self.n:
            heapq.heappush(self.hp, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

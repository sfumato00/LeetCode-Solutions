from ast import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr = arr[0]
        win = 0
        for i, x in enumerate(arr[1:]):
            if curr > x:
                win += 1
            else:
                curr, win = x, 1

            if win == k:
                break
        return curr

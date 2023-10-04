class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        m = len(flowerbed)
        for i in range(m):
            if (
                not flowerbed[i]
                and (i == 0 or not flowerbed[i - 1])
                and (i == m - 1 or not flowerbed[i + 1])
            ):
                n -= 1
                if n == 0:
                    return True
                flowerbed[i] = 1
        return False

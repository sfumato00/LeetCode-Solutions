class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        TOTAL_MINUTES = 12 * 60
        # remainder = hour - 12 * (hour // 12)
        # d1 = (remainder * 60 + minutes) / TOTAL_MINUTES
        d1 = hour % 12 / 12 + minutes / TOTAL_MINUTES
        d2 = minutes / 60

        if d2 > d1:
            d1, d2 = d2, d1
        angle = (d1 - d2) * 360
        return angle if angle <= 180 else 360 - angle

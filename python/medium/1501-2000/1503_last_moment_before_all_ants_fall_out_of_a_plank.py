from typing import List


class Solution:
    """_summary_
    """
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        """The key of this solution is to prove the collision between 2 ants doesn't change the outcome."""
        if not left:
            left = [0]

        if not right:
            right = [n]

        return max(max(left), max([n - r for r in right]))

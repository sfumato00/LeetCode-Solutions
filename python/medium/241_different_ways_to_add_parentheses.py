from functools import lru_cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
        }

        @lru_cache()
        def compute(expr: str) -> List[int]:
            out = []
            for i, x in enumerate(expr):
                if x in ops:
                    for l in compute(expr[:i]):
                        for r in compute(expr[i + 1 :]):
                            out += [ops[x](l, r)]

            if not out:
                return [int(expr)]
            return out

        return compute(expression)

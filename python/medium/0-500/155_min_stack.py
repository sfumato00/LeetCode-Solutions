from math import inf


class MinStack:
    def __init__(self):
        self.stk = []
        self.minn = inf

    def push(self, val: int) -> None:
        if val <= self.minn:
            self.stk += [self.minn]
            self.minn = val
        self.stk += [val]

    def pop(self) -> None:
        if self.stk.pop() == self.minn:
            self.minn = self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minn

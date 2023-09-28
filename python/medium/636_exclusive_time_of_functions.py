class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        fs = [log.split(":") for log in logs]
        callstack = []
        curr = None
        for id, op, ts in fs:
            id = int(id)
            ts = int(ts)
            if op == "start":
                if curr:
                    callstack += [(curr[0], ts)]
                    ans[curr[0]] += ts - curr[1]
                    curr[:] = [id, ts]
                else:
                    curr = [id, ts]
            else:
                ans[curr[0]] += ts - curr[1] + 1
                if callstack:
                    curr[:] = [callstack.pop()[0], ts + 1]
                else:
                    curr = None
        return ans

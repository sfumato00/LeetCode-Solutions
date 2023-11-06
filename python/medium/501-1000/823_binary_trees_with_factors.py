class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 1_000_000_007

        arr.sort()
        mem = {}
        output = 0
        for i, z in enumerate(arr):
            val = 0
            for x in arr[:i]:
                y, r = divmod(z, x)
                if not r and y in mem:
                    val += mem[x] * mem[y] % MOD

            val = (val + 1) % MOD
            output = (output + val) % MOD
            mem[z] = val
        return output

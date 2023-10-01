class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        data = []
        for i in range(m):
            for j in range(n):
                k = i + j
                if k >= len(data):
                    data += [[]]
                data[i + j] += [mat[i][j]]
        out = []
        for k in range(len(data)):
            out += data[k] if k % 2 == 1 else data[k][::-1]
        return out

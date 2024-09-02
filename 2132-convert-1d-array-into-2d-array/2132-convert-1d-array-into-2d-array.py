class Solution:
    def construct2DArray(self, original, m: int, n: int):
        if m * n != len(original):
            return []

        result = [[] for i in range(m)]
        for i in range(m):
            result[i] = original[i * n:(i + 1) * n]
            
        return result

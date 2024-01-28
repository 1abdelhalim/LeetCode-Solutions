class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        cum_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                cum_sum[r+1][c+1] = cum_sum[r+1][c] + cum_sum[r][c+1] - cum_sum[r][c] + matrix[r][c]

     
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                sum_count = {0: 1}
                cur_sum = 0
                for c in range(1, cols + 1):
                    cur_sum = cum_sum[r2][c] - cum_sum[r1-1][c]
                    count += sum_count.get(cur_sum - target, 0)
                    sum_count[cur_sum] = sum_count.get(cur_sum, 0) + 1

        return count
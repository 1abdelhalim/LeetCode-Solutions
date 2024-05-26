class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        def calc_sum(x):
            return x * (x + 1) // 2

        total_sum = calc_sum(n)

        for i in range(1, n + 1):
            left_sum = calc_sum(i)
            right_sum = total_sum - left_sum + i
            if left_sum == right_sum:
                return i

        return -1

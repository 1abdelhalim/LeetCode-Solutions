class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr_str, n_open, n_close):
            if len(curr_str) == 2 * n:
                ans.append(curr_str)
                return

            if n_open < n:
                backtrack(curr_str + '(', n_open + 1, n_close)

            if n_close < n_open:
                backtrack(curr_str + ')', n_open, n_close + 1)

        ans = []
        backtrack('', 0, 0)
        return ans

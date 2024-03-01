class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != '.':
                    ans += [(i, val), (val, j), (i // 3, j // 3, val)]
        return len(ans) == len(set(ans))
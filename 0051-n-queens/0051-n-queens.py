class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        
        board = [['.'] * n for _ in range(n)]  
        cols = set()
        diag_pos = set()
        diag_neg = set()

        def backtrack(r):
            if r == n:
                result.append([''.join(row) for row in board])
                return 

            for col in range(n):
                if col in cols or (r - col) in diag_neg or (r + col) in diag_pos:
                    continue 

                cols.add(col)
                diag_pos.add(r + col)
                diag_neg.add(r - col)
                board[r][col] = 'Q'

                backtrack(r + 1)

                cols.remove(col)
                diag_pos.remove(r + col)
                diag_neg.remove(r - col)
                board[r][col] = '.'

        backtrack(0)
        return result


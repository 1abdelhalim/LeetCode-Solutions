class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for i in range(n)] #n*n baord
        cols = set()
        rows = set()
        diags_pos = set()
        diags_neg = set()

        # define backrack function 

        def backtrack(r):
            # base case 
            # if valid, append and return

            if r == n:
                result.append(["".join(row) for row in board])
                return 


            # iterate 

            for col in range(n):
                # check if valid 
                if col in cols or (r+col) in diags_pos or (r-col) in diags_neg:
                    continue # skip this 

                cols.add(col)
                diags_pos.add(r+col)
                diags_neg.add(r-col)
                board[r][col] = "Q" 

                # go a foraward step 
                backtrack(r+1)
                cols.remove(col)
                diags_pos.remove(r+col)
                diags_neg.remove(r-col)
                board[r][col] = "." 

        backtrack(0) #index
        return result 
            
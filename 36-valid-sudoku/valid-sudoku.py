class Solution(object):
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            if not self.is_valid_row(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[i][col] for i in range(9)]
            if not self.is_valid_row(column):
                return False
        
        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid_row(sub_box):
                    return False
        
        return True

    def is_valid_row(self, row):
        seen = set()
        for cell in row:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
        return True
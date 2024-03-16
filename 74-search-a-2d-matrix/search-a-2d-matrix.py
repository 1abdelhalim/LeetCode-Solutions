class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        left = 0 
        right = n * m - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // m
            mid_col = mid % m
            mid_val = matrix[mid_row][mid_col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # Difine the max_diag var
        # Get length of each diag 
        # Loop and update 
        # If current > max  then update 
        # if current = max and area > then also update 
        import math 
        def diag(l, w):
            diag = math.sqrt(l**2 + w**2)
            return diag 
            

        def area(l, w):
            area = l * w 
            return area

        max_diag = diag(dimensions[0][0], dimensions[0][1])
        result_area = area(dimensions[0][0], dimensions[0][1])

        n = len(dimensions)
        for i in range(1, n):
            length = dimensions[i][0] 
            width = dimensions [i][1]
            curr_diag = diag(length, width) 
            curr_area = area(length, width) 

            if curr_diag > max_diag:
                max_diag = curr_diag
                result_area = curr_area

            elif curr_diag == max_diag:
                result_area = max(curr_area, result_area)


        return result_area
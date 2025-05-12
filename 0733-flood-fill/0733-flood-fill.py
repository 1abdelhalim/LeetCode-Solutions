class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        init_color = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def paint(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if image[i][j] != init_color:
                return

            image[i][j] = color
            paint(i-1, j)
            paint(i+1, j)
            paint(i, j-1)
            paint(i, j+1)

        paint(sr, sc)
        return image

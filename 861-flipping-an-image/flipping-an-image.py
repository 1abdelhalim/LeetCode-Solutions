class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for i in range(n):
            image[i] = image[i][::-1]
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1 
                else:
                    image[i][j] = 0

        return image
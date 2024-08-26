class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)

        if  n < 3:
            return [] 

        result = []
        i, j, k = 0, 1, 2
        
        while k < n:
            if (words[i] == first and words[j] == second):
                result.append(words[k])

            i += 1 
            j += 1 
            k += 1 

        return result 

        

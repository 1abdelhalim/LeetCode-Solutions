class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon
        from collections import Counter
        counter = Counter(text)

        result = 0 
        print(counter)
        n = len(text)
        for i in range(n):
            if (counter["l"] >= 2 and counter["o"] >= 2 and counter["n"] >= 1 and counter["a"] >= 1 and counter["b"] >= 1):
                result += 1
                counter["l"] -= 2
                counter["o"] -= 2
                counter["n"] -= 1 
                counter["a"] -= 1
                counter["b"] -= 1

        return result 

        


from collections import defaultdict 

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes) 
        result = 0 
        counter = defaultdict(int) 

        for a,b in dominoes:
            key = tuple(sorted((a,b)))
            result += counter[key]

            counter[key] += 1 

        return result 
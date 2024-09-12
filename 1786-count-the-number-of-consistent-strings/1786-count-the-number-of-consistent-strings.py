class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count  = 0 
        chars = {}
        flag = True 

        for word in words:
            if all(ch in allowed for ch in word):
                count += 1 

        return count 

            
            
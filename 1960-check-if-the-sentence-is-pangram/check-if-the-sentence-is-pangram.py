class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
        if set(sentence) == alphabet_set:
            return True 
        
        return False 
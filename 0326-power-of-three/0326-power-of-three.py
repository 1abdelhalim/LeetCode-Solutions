class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True 
            
        if n < 3:
            return False 
        
        rem = n / 3 
        while rem % 3 == 0:
            rem = rem / 3 

        if rem == 1:
            return True 
        
        return False
class Solution:
    def canWinNim(self, n: int) -> bool:

        if n <= 3:
            return True 

        elif n % 4 == 0:
            return False 

        return True 

        # 1 >> T 
        # 2 >> T 
        # 3 >> T 
        # 4 >> F 
        # 5 >> T 
        # 6 >> T  
        # 7 >> T
        # 8 >> F  

        # 5 :
        # 1 
        # 
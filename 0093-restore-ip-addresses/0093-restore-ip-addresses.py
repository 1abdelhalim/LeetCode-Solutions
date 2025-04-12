class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        
        if n < 4 or n > 12: #not valid  
            return [] 

        def is_valid(substr: str) -> bool:
            if len(substr) > 3:
                return False
                
            if not (0 <= int(substr) <= 255):
                return False
                
            if substr != "0" and substr[0] == "0":
                return False
    
            return True

        result = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == n:
                    result.append(".".join(path))  
                return
            
            for i in range(1, 4):
                if start + i <= n:
                    segment = s[start:start + i]
                    if is_valid(segment):
                        backtrack(start + i, path + [segment])

        backtrack(0, [])
        return result

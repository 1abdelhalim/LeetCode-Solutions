class Solution:
    def validStrings(self, n: int) -> List[str]:
        valid_strs = []

        def backtrack(curr_str):
            if len(curr_str) == n:
                valid_strs.append(curr_str)
                return
            backtrack(curr_str + '1')
 
            if not curr_str or curr_str[-1] != '0':
                backtrack(curr_str + '0')
                
        backtrack("")
        
        return valid_strs
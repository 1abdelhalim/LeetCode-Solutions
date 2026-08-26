import itertools
class Solution:
    def validStrings(self, n: int) -> List[str]:
       count = 0 
       if n == 1:
        return ["0","1"]

       comps =  itertools.product('01', repeat=n)
       bin_strs = [''.join(comp) for comp in comps]

       valid_strs = []
       for bin_str in bin_strs:
           if "00" not in bin_str:
               valid_strs.append(bin_str)
        
       return valid_strs
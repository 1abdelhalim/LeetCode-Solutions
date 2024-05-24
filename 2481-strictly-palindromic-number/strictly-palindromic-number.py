class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base_n(decimal_number, base):
            if decimal_number == 0:
                return '0'

            digits = []
            while decimal_number:
                remainder = decimal_number % base
                digits.append(str(remainder))
                decimal_number //= base
                
            return ''.join(digits[::-1])


        def is_palindrome(num):
            return str(num) == str(num)[::-1]
            
        flag = True
        
        for i in range(2, n-1):
            if is_palindrome(to_base_n(n, i)) == False:
                flag = False
                break

        print(flag)

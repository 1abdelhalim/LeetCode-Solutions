class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(string: str) -> bool:
            return string == string[::-1]
        
        result = []
        def backtrack(string:str):
            
            stack = [(0, [])]
            n = len(s)

            while stack:
                start, path = stack.pop()

                if start == n:
                    result.append(path)
                    continue 


                for i in range(start+1, n+1):
                    sub = s[start:i]

                    if is_palindrome(sub):
                        stack.append((i, path+[sub]))

        backtrack(s)
        return result 


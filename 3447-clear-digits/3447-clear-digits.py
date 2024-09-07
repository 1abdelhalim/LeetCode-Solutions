class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for dig in s:
            if stack and dig.isdigit() and not stack[-1].isdigit():
                stack.pop()  
            else:
                stack.append(dig)   
        return "".join(stack)

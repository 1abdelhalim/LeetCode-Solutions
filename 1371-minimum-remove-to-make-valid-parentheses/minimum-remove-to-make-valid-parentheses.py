class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = []

        for ch in s:
            if ch == ")":
                if stack:
                    stack.pop()
                    result.append(ch)
            elif ch == "(":
                stack.append(len(result))
                result.append(ch)
            else:
                result.append(ch)

        for index in stack:
            result[index] = ''

        return ''.join(result)

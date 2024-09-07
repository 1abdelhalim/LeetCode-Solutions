class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if stack and log == "../":
                stack.pop()
            elif log == "./" or log == ",":
                continue
            elif log == "../":
                continue
            else:
                stack.append(log)

        print(stack)
        return len(stack)
                

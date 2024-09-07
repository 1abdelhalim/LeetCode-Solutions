class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []

        for op in operations:
            if op == "+":
                result.append(result[-1] + result[-2]) 
            elif op == "D":
                result.append(2 * result[-1]) 
            elif op == "C":
                result.pop()  
            else:
                result.append(int(op))  

        return sum(result)

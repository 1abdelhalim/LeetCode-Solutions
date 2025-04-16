class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = [""]  # start with an empty string

        for digit in digits:
            temp = []
            for combo in result:
                for char in letters[digit]:
                    temp.append(combo + char)
            result = temp

        return result

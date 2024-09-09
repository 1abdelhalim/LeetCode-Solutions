class Solution:
    def convertDateToBinary(self, date: str) -> str:
        splitted_date = date.split("-")
        splitted_date = [bin(int(x))[2:] for x in splitted_date]
        
        return "-".join(splitted_date)

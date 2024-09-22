class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_num = bin(num)[2:]
        count_ones = bin_num.count("1")

        return count_ones*2 
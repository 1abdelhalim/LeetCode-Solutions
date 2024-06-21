class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        max_add = add = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                add += customers[i]

        max_add = add

        for i in range(minutes, n):
            if grumpy[i] == 1:
                add += customers[i]
            if grumpy[i - minutes] == 1:
                add -= customers[i - minutes]
            
            max_add = max(max_add, add)

   
        return satisfied + max_add
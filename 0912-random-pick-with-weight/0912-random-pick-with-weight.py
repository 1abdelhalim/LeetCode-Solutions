import random
import bisect
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix.append(current_sum)
        self.total = current_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)

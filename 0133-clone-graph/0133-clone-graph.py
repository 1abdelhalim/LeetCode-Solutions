"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, x: Optional['Node']) -> Optional['Node']:
        if not x:
            return x
        a = {}
        def b(c):
            if c in a:
                return a[c]
            d = Node(c.val)
            a[c] = d
            for e in c.neighbors:
                d.neighbors.append(b(e))
            return d
        return b(x)
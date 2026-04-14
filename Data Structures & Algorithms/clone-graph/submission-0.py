"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.hashMap = {}

        def dfs(node):
            if not node:
                return None
            if node in self.hashMap:
                return self.hashMap[node]

            new_item = Node(node.val)
            self.hashMap[node] = new_item

            for neighbor in node.neighbors:
                new_item.neighbors.append(dfs(neighbor))

            return new_item

        return dfs(node)

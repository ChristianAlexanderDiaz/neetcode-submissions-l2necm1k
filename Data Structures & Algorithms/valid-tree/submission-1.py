class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        roots = set()

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        for a, b in edges:
            if (union(a, b) == False):
                return False
            
        for i in range(n):
            roots.add(find(i))

        return len(roots) == 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            parent[ry] = rx
            return True

        for a, b in edges:
            union(a, b)

        for i in range(n):
            roots.add(find(i))
        
        return len(roots)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, (x,y)))
        
        while len(result) < k:
            tuple = heapq.heappop((heap))
            result.append(tuple[1])

        return result
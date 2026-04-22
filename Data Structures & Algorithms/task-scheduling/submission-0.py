class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # minNum
        self.minNum = 0

        # counter
        c = Counter(tasks)
        print(c)

        # heap
        heap = []
        for num in c.values():
            heapq.heappush(heap, -num)
        print(heap)
        
        # queue
        queue = deque([])

        time = 0

        while heap or queue:
            time += 1

            if heap:
                count = -heapq.heappop(heap)
                count -= 1
                if count > 0:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                released_count = queue.popleft()[0]
                heapq.heappush(heap, -released_count)

        return time



        return 0
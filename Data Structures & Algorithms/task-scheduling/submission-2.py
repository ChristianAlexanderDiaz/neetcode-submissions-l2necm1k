class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
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
        print(queue)

        time = 0
        while heap or queue:
            time += 1
            if heap:
                count = -heapq.heappop(heap)
                count -= 1
                # next time we run it
                if count > 0:
                    queue.append([count, time + n])

            # if there is something in the queue and the (time + n) ^ is the time, its time to add back to the queue
            if queue and queue[0][1] == time:
                replaced_count = queue.popleft()[0]
                heapq.heappush(heap, -replaced_count)

        print(time)

        # return time
        return time

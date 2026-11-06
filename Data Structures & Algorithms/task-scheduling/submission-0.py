from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        # Count how many times each task appears
        count = Counter(tasks)

        # Max heap (use negative values because Python has min heap)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # stores (count, time_when_available)

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # use one task

                if cnt != 0:
                    # put it in cooldown
                    cooldown.append((cnt, time + n))

            # if any task finished cooldown, push it back
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time
        
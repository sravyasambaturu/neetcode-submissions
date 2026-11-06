from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list graph and fill the indegree array
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            
        # 2. Add all courses with 0 prerequisites to our starting queue
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        taken = 0
        
        # 3. Process the queue level by level (BFS)
        while queue:
            cur = queue.popleft()
            taken += 1
            
            # Decrement prerequisite count for all courses depending on 'cur'
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                # If a course has 0 prerequisites left, it's unlocked!
                if indegree[nxt] == 0:
                    queue.append(nxt)
                    
        # 4. If we successfully took all courses, return True. Otherwise False (cycle detected).
        return taken == numCourses








# 💡 The Core Concept: The Dependency Checklist

# Think of this like unlocking achievements in a video game or clearing requirements for a college major:
# • If a course has an indegree of 0, it means it has no prerequisites (or you've already taken them all). You can take it immediately!
# • Every time you finish a course, you check all the future courses that relied on it, and you cross off that prerequisite requirement from their checklist (subtract 1 from their indegree).
# • If a future course hits 0 prerequisites left, you unlock it and add it to your queue of courses you can take next.

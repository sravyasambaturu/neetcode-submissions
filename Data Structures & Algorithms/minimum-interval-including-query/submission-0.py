class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(intervals) 
        heap = []  # Stores tuples of (size, right_end)
        result = {} 
        i = 0 
        
        # **Sort the queries to process them in chronological order**
        for q in sorted(queries): 
        # 1. Add every interval that starts at or before the current query position 'q'
            while i < len(items) and items[i][0] <= q:
                l, r = items[i] 
                heapq.heappush(heap, (r - l + 1, r)) 
                i += 1 
                
            # 2. Drop intervals from the top of the heap if they ended strictly before 'q'
            while heap and heap[0][1] < q:  
                heapq.heappop(heap) 
                
            # 3. If heap is not empty, the root holds the smallest valid interval size
            result[q] = heap[0][0] if heap else -1 
            
        # Return the results mapped back to the original order of the queries
        return [result[q] for q in queries]

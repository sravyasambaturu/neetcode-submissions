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



# example walkthrough

# 1. Processing Query q = 1

# • While Loop 1 (Add valid intervals): Does items[0][0] (1) ≤ q (1)? Yes.
# 	• Interval [1, 3] has size 3 - 1 + 1 = 3, right boundary r = 3.
# 	• Push (3, 3) to heap. i becomes 1.
# 	• Does items[1][0] (2) ≤ q (1)? No. Loop exits.
# • While Loop 2 (Remove expired intervals): heap[0][1] (3) < q (1)? No.
# • Record Result: Top of heap is (3, 3). Smallest size is 3.
# • result[1] = 3

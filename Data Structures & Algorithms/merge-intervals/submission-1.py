class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for start, end in sorted(intervals):
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result

# • Sort by start. Now any interval can only overlap with the ones just before it. 
# • Keep a result list. For each interval (start, end): 
# o If the result is not empty and start <= result[-1][1] (it starts before the last one 
# ends), they overlap: update the last end: result[-1][1] = max(result[-1][1], 
# end). 
# o Otherwise, add [start, end] as a new interval. 
# • Use max for the end, because the new interval can be completely inside the last one (like [1,10] 
# and [2,3]). 
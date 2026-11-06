class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)
        #1 everything that ends before the new one starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        start, end = newInterval
        #2 everything that overlaps grow the new interval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])
        #3 everything after the new one ends
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
        



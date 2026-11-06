class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
#add all previous intervals
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

#merge all the intervals that overlap
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

#add all remaining intervals that comes after
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
        
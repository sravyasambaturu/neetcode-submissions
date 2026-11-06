class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end  = intervals[0][1]
        for current in intervals[1:]:
            current_start, current_end = current
            if current_start < prev_end:
                count += 1
                prev_end = min(prev_end, current_end)
            else:
                prev_end = current_end

        return count
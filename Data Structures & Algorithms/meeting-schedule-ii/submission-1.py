"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # starts = sorted(s for s, _ in intervals)
        # ends = sorted(e for _, e in intervals)
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        rooms = best = 0
        j = 0 
        for s in starts:
            while ends[j] <= s:
                j += 1
                rooms -= 1
            rooms += 1
            best = max(best, rooms)
        return best





# In Python, the single underscore (_) is used as a throwaway variable name to indicate that a specific value is being ignored.
# In your code, it appears in two list comprehensions:
# 1. s for s, _ in intervals
# 2. e for _, e in intervals

# Why it is used here

# The intervals list contains pairs of numbers representing the start and end times of a meeting (e.g., [start_time, end_time]).
# • When extracting the start times, the code only cares about the first element (s). It uses _ for the second element because the end time doesn't matter for that specific list.
# • When extracting the end times, the code only cares about the second element (e). It uses _ for the first element because the start time is irrelevant there.

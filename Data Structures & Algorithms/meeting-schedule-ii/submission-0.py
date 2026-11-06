"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        max_rooms = 0
        current_rooms = 0

        s,e = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                current_rooms += 1
                s += 1
            else:
                current_rooms -= 1
                e += 1

            max_rooms = max(max_rooms, current_rooms)

        return max_rooms



        
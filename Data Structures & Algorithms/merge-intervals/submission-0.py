class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for current in intervals[1:]:
        # If current start <= previous end, they overlap
            if current[0] <= merged[-1][1]:
            # Merge them by updating the end time
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
            # No overlap, just add it to the list
                merged.append(current)

        return merged


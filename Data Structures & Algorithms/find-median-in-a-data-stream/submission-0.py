from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # max heap (store negative values)
        # holds the smaller half
        self.small = []

        # min heap
        # holds the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # STEP 1: always push into max heap first
        heappush(self.small, -num)

        # STEP 2: make sure ordering is correct
        # (largest in small should not be greater than smallest in large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large, val)

        # STEP 3: balance sizes

        # if small is too big
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)

        # if large is bigger
        if len(self.large) > len(self.small):
            val = heappop(self.large)
            heappush(self.small, -val)

    def findMedian(self) -> float:
        # if odd → small heap has extra element
        if len(self.small) > len(self.large):
            return -self.small[0]

        # if even → average of two middle values
        return (-self.small[0] + self.large[0]) / 2
        
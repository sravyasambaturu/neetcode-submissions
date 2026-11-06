class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        result = [] 
        dq = deque()  # stores indices; values decrease from front to back 
        for i, x in enumerate(nums): 
            while dq and nums[dq[-1]] <= x: 
                dq.pop() 
            dq.append(i) 
            if dq[0] <= i - k: 
                dq.popleft() 
            if i >= k - 1: 
                result.append(nums[dq[0]]) 
        return result 
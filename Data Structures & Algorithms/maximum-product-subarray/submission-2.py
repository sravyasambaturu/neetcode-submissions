class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    # Global result tracker initialized with the first number
        res = nums[0]
    
    # Track the current min and max products ending at the current position
        curr_min, curr_max = 1, 1
    
        for n in nums:
            # If we encounter a 0, it resets our streak. 
            # Handled naturally by evaluating 'n' as a fresh starting choice below.
            
            # We store curr_max in a temp variable because its value changes,
            # but we still need the old value to calculate curr_min.
            tmp = curr_max * n
            
            # Three choices for the new max/min:
            # 1. Multiply the number with the previous max
            # 2. Multiply the number with the previous min (negative * negative)
            # 3. Start a brand new subarray from the current number 'n'
            curr_max = max(tmp, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)
            
            # Update our ultimate global maximum answer
            res = max(res, curr_max)
            
        return res

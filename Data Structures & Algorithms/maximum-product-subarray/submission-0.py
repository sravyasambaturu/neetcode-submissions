class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, current * max_so_far, current * min_so_far)
            min_so_far = min(current, current * max_so_far, current * min_so_far)
            max_so_far = temp_max
            result = max(result, max_so_far)
    
        return result
        
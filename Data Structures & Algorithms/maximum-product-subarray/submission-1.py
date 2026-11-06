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

# Walkthrough with [2, 3, -2, 4]
# Initial: max_so_far = 2, min_so_far = 2, result = 2
# i = 1, current = 3:

# temp_max = max(3, 3×2, 3×2) = max(3, 6, 6) = 6
# min_so_far = min(3, 6, 6) = 3
# max_so_far = 6
# result = max(2, 6) = 6

# i = 2, current = -2:

# temp_max = max(-2, -2×6, -2×3) = max(-2, -12, -6) = -2
# min_so_far = min(-2, -12, -6) = -12
# max_so_far = -2
# result = max(6, -2) = 6

# i = 3, current = 4:

# temp_max = max(4, 4×-2, 4×-12) = max(4, -8, -48) = 4
# min_so_far = min(4, -8, -48) = -48
# max_so_far = 4
# result = max(6, 4) = 6

# Answer: 6 ✓
# Notice why we track min_so_far: at i=2, the min became -12. If a -1 came next, that -12 × -1 = 12 would beat everything.
        
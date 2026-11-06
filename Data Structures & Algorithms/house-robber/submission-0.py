class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def solve(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            # not rob
            temp_left = solve(i + 1)

            # rob
            temp_right = nums[i] + solve( i + 2 )

            memo[i] = max(temp_right, temp_left)

            return memo[i]

        return solve(0)
        
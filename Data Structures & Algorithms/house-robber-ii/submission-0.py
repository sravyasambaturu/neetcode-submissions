class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def solve(i, take_first):

            if i >= len(nums) or (i == len(nums) - 1 and take_first):
                return 0

            if (i, take_first) in memo:
                return memo[(i, take_first)]

            #choice not take 

            left = solve(i + 1, take_first)

            #choice take 

            right = nums[i] + solve(i + 2, take_first or i == 0 )

            memo[(i, take_first)] = max(left, right)

            return memo[(i, take_first)]

        return solve(0, False)
        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dicti = {}
        def solve(i, value):
            if value == target and i == len(nums):
                return 1
            
            if (i, value) in dicti:
                return dicti[(i, value)]
            
            if i == len(nums):
                return 0
            
            temp = solve(i + 1, value + nums[i]) + solve(i + 1, value - nums[i])

            dicti[(i, value)] = temp
            return temp
        
        return solve(0, 0)
        
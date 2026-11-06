class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ % 2 !=0:
            return False
        
        half_sum = summ // 2

        memo = {}

        def dfs(i, temp):

            if (i, temp) in memo:
                return memo[(i, temp)]

            if i == len(nums) or temp > half_sum:
                return False

            if temp == half_sum:
                return True


            #not take
            left = dfs(i + 1, temp)

            #take
            right = dfs(i + 1, temp + nums[i])

            memo[(i, temp)] = left or right

            return memo[(i, temp)]
        
        return dfs(0, 0)
        
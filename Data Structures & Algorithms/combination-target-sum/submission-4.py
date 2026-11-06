class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            #base case if we successfully hit our target Sum
            if total == target:
                res.append(curr.copy())
                return 

            #we went over the target or we ran out of numbers
            if total > target or i >= len(nums):
                return 

            #choose to include nums[i]
            curr.append(nums[i])
            #stay at i so that we can reuse
            dfs(i, curr, total + nums[i])

            #backtrack: cleaning up the current choice before we move to second choice
            curr.pop()

            #skip the choice and move to next index
            dfs(i+1, curr, total)

        #start the recursive search with i = 0, empty [] and sum = 0
        dfs(0, [], 0)
        return res
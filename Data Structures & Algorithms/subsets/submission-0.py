class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, nums, temp):
            if index == len(nums):
                res.append(temp[::])
                return

            temp.append(nums[index])
            dfs(index + 1, nums, temp)
            temp.pop()
            dfs(index + 1, nums, temp)
        
        # for i in range(len(nums)):
        dfs(0, nums, [])

        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, target):
            if target == 0:
                res.append(path[:])
                return 
            if i == len(nums) or target < 0:
                return
   
            #pick the ele
            path.append(nums[i])
            dfs(i, path, target - nums[i]) 
            #not pick the ele
            path.pop()
            dfs(i+1, path, target)
            return 
        
        dfs(0, [], target)
        return res
        
         

    #     2     []  i = 0 
    #     2,2        i = 0
    # res = []
    #     if target == 0:
    #         res.append(path[:])
    #         return 
    #     if i == len(nums):
    #         return


    #       path.append(nums[i])
    #    #pick  dfs(i, path, target - nums[i]) 
    #       path.pop()
    #    #not pick dfs(i+1, path, target)
    #      #pick 
    #      #not pick 

    # return res
      
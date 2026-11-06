# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         memo = {}

#         def solve(i, j):
#             if i == len(nums):
#                 return 0
#             if (i,j) in memo:
#                 return memo[(i,j)] 
            
#             #skip 
#             res = solve(i + 1, j)

#             #don't skip
#             if j == -1 or nums[j] < nums[i]:
#                 res = max(res, 1 + solve(i+1, i))
            
#             memo[(i,j)] = res 

#             return res

#         return solve(0, -1)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(10000)
        memo = {}
        
        def solve(i, j):
            if i == len(nums):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # skip
            res = solve(i + 1, j)

            # don't skip
            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + solve(i + 1, i))

            memo[(i, j)] = res
            return res

        return solve(0, -1)

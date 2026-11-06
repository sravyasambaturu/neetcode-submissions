class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                #pruning
                if candidates[i] > target:
                    break

                #pick the ele
                path.append(candidates[i])
                dfs(i + 1, path, target - candidates[i])
                #not pick the ele
                path.pop()

        dfs(0, [], target)
        return res
        
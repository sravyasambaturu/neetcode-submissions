class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dicti = {}
        def solve(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if (i, j, k) in dicti:
                return dicti[(i, j, k)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = solve(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                res = res or solve(i, j + 1, k + 1)
            
            dicti[(i, j, k)] = res
            return dicti[(i, j, k)]
         

        return solve(0, 0, 0)
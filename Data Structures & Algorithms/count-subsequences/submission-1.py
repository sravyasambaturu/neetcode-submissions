class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        dicti  = {}


        def solve(i, j):
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in dicti:
                return dicti[(i, j)]

            #not take
            res = solve(i + 1, j)
            #take
            if s[i] == t[j]:
                res+= solve(i + 1, j + 1) 

            dicti[(i, j)] = res

            return res  
        
        return solve(0, 0)
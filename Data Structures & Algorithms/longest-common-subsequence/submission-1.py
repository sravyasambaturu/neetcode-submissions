class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dictt = {}
        def solve(i, j):
        
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in dictt:
                return dictt[(i, j)]

            if text1[i] == text2[j]:
                dictt[(i, j)] =  1 + solve(i + 1, j + 1)
            else:
                left = solve(i + 1, j)
                right = solve(i, j + 1)
                dictt[(i, j)] = max(left, right)
            
            return dictt[(i, j)]
        
        return solve(0, 0)
        
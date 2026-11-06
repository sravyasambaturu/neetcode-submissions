class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dicti = {}

        def solve(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j ) in dicti:
                return dicti[(i,j)]

            if word1[i] == word2[j]:
                dicti[(i,j)] = solve(i + 1, j + 1)
            else: 
                res = min(1 + solve(i, j + 1), 1 + solve(i + 1, j))
                res =  min(res, 1 + solve(i + 1, j + 1))
                dicti[(i,j)] = res
            return dicti[(i,j)]

        return solve(0, 0)

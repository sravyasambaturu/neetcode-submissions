class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        # memo = {}
        count = [0]
        def solve(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count[0]+=1
                l = l - 1
                r = r + 1
            
            # return l + 1, r - 1

        # start = 0
        # end = 0

        for i in range(len(s)):
            solve(i, i) # odd length
            solve(i, i + 1) # even length

            # if r1 - l1 > end - start:
            #     start = l1 
            #     end = r1
            
            # if r2 - l2 > end - start:
            #     start = l2
            #     end = r2
        
        return count[0]
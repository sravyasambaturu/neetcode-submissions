class Solution:
    def numDecodings(self, s: str) -> int:
        mapp = {}


        def solve(i):

            if i in mapp:
                return mapp[i]

            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0
            
            if s[i] in '123456789':
                mapp[i] = solve(i + 1)

            if i < len(s) - 1 and ((s[i] == '1') or (s[i] == '2' and s[i+1] in '0123456')):
                mapp[i]+=solve(i + 2) 

            return mapp[i]

        return solve(0)

        
        
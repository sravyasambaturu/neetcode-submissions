class Solution:
    def numDecodings(self, s: str) -> int:
        mapp = {}
        
        def solve(i: int) -> int:
            # 1. Check if we already computed this subproblem
            if i in mapp:
                return mapp[i]
                
            # 2. Base Case: Successfully reached the end of the string
            if i >= len(s):
                return 1
                
            # 3. Base Case: Single '0' cannot be decoded
            if s[i] == "0":
                return 0
                
            # Initialize a counter for valid decoding paths from index i
            ways = 0
            
            # Choice 1: Decode as a single digit (1-9)
            if s[i] in '123456789':
                ways += solve(i + 1)
                
            # Choice 2: Decode as a double digit (10-26)
            if i < len(s) - 1 and ((s[i] == '1') or (s[i] == '2' and s[i+1] in '0123456')):
                ways += solve(i + 2)
                
            # Save the result to our map and return it
            mapp[i] = ways
            return mapp[i]
            
        return solve(0)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
        



# The GoalIf the input is n = 5, LeetCode wants you to look at every number from 0 all the way up to 5. For each of those numbers, count how many 1s are in its binary form, and put those counts into a list. Let's look at the numbers 0 through 5 manually: 
# 0 in binary is 0000 -> 0 ones
# 1 in binary is 0001 -> 1 one
# 2 in binary is 0010 -> 1 one
# 3 in binary is 0011 -> 2 ones
# 4 in binary is 0100 -> 1 one
# 5 in binary is 0101 -> 2 ones 
# So, if n = 5, your code should return the list: [0, 1, 1, 2, 1, 2]. 
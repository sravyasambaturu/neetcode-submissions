class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# Let's trace it with nums = [1, 2, 3, 4].
# Initial State:
# res = [1, 1, 1, 1]
# Pass 1: Prefix (Left to Right)
# • i = 0 (num = 1): res[0] = prefix → res[0] = 1. Update prefix = 1 * 1 = 1.
# • i = 1 (num = 2): res[1] = prefix → res[1] = 1. Update prefix = 1 * 2 = 2.
# • i = 2 (num = 3): res[2] = prefix → res[2] = 2. Update prefix = 2 * 3 = 6.
# • i = 3 (num = 4): res[3] = prefix → res[3] = 6. Update prefix = 6 * 4 = 24.
# Array state after prefix pass: res = [1, 1, 2, 6]
# (Notice each element is the product of everything to its left!)
# Pass 2: Postfix (Right to Left)
# • i = 3 (num = 4): res[3] *= postfix → 6 * 1 = 6. Update postfix = 1 * 4 = 4.
# • i = 2 (num = 3): res[2] *= postfix → 2 * 4 = 8. Update postfix = 4 * 3 = 12.
# • i = 1 (num = 2): res[1] *= postfix → 1 * 12 = 12. Update postfix = 12 * 2 = 24.
# • i = 0 (num = 1): res[0] *= postfix → 1 * 24 = 24. Update postfix = 24 * 1 = 24.
# Final Array: res = [24, 12, 8, 6]
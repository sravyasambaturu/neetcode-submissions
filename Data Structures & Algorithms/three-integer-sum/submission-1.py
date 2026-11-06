class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sorting is critical for the two-pointer approach

        for i, a in enumerate(nums):
            # If the current number is positive, it's impossible to sum to 0 with numbers to its right
            if a > 0:
                break
                
            # Skip the same value as the previous element to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Two-pointer setup for the remaining part of the array
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1  # Sum is too big, decrease the right value
                elif threeSum < 0:
                    left += 1   # Sum is too small, increase the left value
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the left pointer to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res

        
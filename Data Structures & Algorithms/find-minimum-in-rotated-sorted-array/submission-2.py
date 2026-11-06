class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_val = nums[-1]
        low = 0
        high = len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > last_val:
                low = mid + 1
            else:
                ans = mid 
                high = mid - 1
        return nums[ans]
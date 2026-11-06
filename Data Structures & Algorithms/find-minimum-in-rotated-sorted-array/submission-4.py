class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]




        # last_val = nums[-1]
        # low = 0
        # high = len(nums) - 1
        # ans = -1
        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] > last_val:
        #         low = mid + 1
        #     else:
        #         ans = mid 
        #         high = mid - 1
        # return nums[ans]
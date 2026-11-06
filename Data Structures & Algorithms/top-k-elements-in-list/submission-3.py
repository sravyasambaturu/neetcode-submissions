class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #bucket sort
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num,cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


# Let's trace it with nums = [1, 1, 1, 2, 2, 100] and k = 2.
# 1. Count Frequencies:
# count = {1: 3, 2: 2, 100: 1}
# 2. Fill Buckets (freq of size 6 + 1 = 7):
# 	• Index 0: []
# 	• Index 1 (appears once): [100]
# 	• Index 2 (appears twice): [2]
# 	• Index 3 (appears thrice): [1]
# 	• Index 4, 5, 6: []
# freq = [[], [100], [2], [1], [], [], []]
# 3. Gather Results (Iterating backwards from index 6 to 1):
# 	• Index 6, 5, 4 are empty.
# 	• Index 3 has [1]. res = [1].
# 	• Index 2 has [2]. res = [1, 2].
# 	• len(res) == 2 (which matches k). Return [1, 2]
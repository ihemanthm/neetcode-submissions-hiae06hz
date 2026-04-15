from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        doublet_mapping = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                total = nums[i]+nums[j]
                doublet_mapping[total].append((i,j))
        res = list()
        for idx, num in enumerate(nums):
            rem = -num
            doublets = doublet_mapping.get(rem, [])
            if doublets:
                for pair in doublets:
                    if idx in pair:
                        continue
                    res.append([nums[idx], nums[pair[0]], nums[pair[1]]])
        unique = set()
        for triplet in res:
            unique.add(tuple(sorted(triplet)))
        return [list(i) for i in unique]
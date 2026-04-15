class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapper = dict()
        for idx, num in enumerate(nums):
            rest = target-num
            if rest in index_mapper:
                return [index_mapper[rest], idx]
            index_mapper[num] = idx
        return [-1, -1]
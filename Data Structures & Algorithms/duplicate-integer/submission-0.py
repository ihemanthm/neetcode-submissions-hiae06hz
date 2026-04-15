class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_length = len(nums)
        unique_nums = list(set(nums))
        unique_length = len(unique_nums)
        return original_length!=unique_length
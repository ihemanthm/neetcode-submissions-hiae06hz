class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            res = res ^ num
        return res^1
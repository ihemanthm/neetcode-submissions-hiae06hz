class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        longest_sequence = 0
        for num in nums:
            if num-1 not in nums_hash:
                length = 1
                while num+length in nums_hash:
                    length+=1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence
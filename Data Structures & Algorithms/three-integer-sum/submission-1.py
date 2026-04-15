from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for idx, num in enumerate(nums):
            target = -num
            left, right = idx+1, len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target:
                    res.add((nums[left], nums[right], num))
                    right-=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        final_res = [list(each) for each in res]
        return final_res
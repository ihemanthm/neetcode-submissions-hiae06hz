class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        n = len(nums)
        
        if zero_count > 1:
            return [0]*n
        
        tot_prod = 1
        prod_without_zero = 1
        for num in nums:
            tot_prod*=num
            if num!=0:
                prod_without_zero*=num
        res = []
        for num in nums:
            if num==0:
                res.append(prod_without_zero)
                continue
            res.append(tot_prod//num)
        return res
        

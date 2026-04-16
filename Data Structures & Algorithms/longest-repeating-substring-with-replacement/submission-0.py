class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict()
        res, left = 0,0
        maxFreq = 0
        for right, each in enumerate(s):
            counts[each] = counts.get(each, 0)+1
            maxFreq = max(maxFreq, counts[each])
            while ((right-left+1)-maxFreq>k):
                counts[s[left]]-=1
                left+=1
            res = max(res, right-left+1)
        return res
            

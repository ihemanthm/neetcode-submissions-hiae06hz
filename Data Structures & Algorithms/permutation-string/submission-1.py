class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = dict()
        for each in s1:
            s1_counts[each] = s1_counts.get(each,0)+1
        
        source_length = len(s1)
        left, right = 0,0
        s2_counts = dict()
        while right<len(s2):
            s2_counts[s2[right]] = s2_counts.get(s2[right], 0)+1
            if (right-left+1)>source_length:
                s2_counts[s2[left]]-=1
                if s2_counts[s2[left]]==0:
                    del s2_counts[s2[left]]
                left+=1
                
            if s1_counts == s2_counts:
                return True
            right+=1
        return False

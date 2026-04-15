from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_mapper = defaultdict(list)
        for each in strs:
            sorted_str = ''.join(sorted(each))
            str_mapper[sorted_str].append(each) 
        
        res = list()
        for key, val in str_mapper.items():
            res.append(list(val))
        return res
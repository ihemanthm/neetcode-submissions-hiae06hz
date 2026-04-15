class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_mapper = dict()
        for each in strs:
            sorted_str = ''.join(sorted(each))
            if sorted_str not in str_mapper:
                str_mapper[sorted_str] = list()
            str_mapper[sorted_str].append(each) 
        
        res = list()
        for key, val in str_mapper.items():
            res.append(list(val))
        return res
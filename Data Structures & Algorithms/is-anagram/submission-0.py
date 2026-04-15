class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper = dict()
        for each in s:
            mapper[each] = mapper.get(each, 0)+1
        
        for each in t:
            mapper[each] = mapper.get(each,0)-1
        
        for key, val in mapper.items():
            if val!=0:
                return False
        return True
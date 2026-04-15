from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_mapper = defaultdict(list)
        for each in strs:
            counts = [0]*26
            for i in each:
                counts[ord(i)-ord('a')]+=1
            str_mapper[tuple(counts)].append(each)
        return [group for _, group in str_mapper.items()]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_mapper = dict()
        left, res = 0, 0
        for right, each in enumerate(s):
            if each in char_mapper:
                left = max(char_mapper[each]+1, left)
            char_mapper[each] = right
            res = max(res, right-left+1)
        return res

            
class Solution:
    def create_one_hot(self, s) -> str:
        one_hot_vect = [0]*26
        for each in s:
            one_hot_vect[ord(each)-ord('a')]+=1        
        return one_hot_vect

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_one_hot = self.create_one_hot(s1)
        source_length = len(s1)

        left, right = 0, source_length-1
        while right<len(s2):
            substr_one_hot = self.create_one_hot(s2[left:right+1])
            if substr_one_hot == s1_one_hot:
                return True
            left, right = left+1, right+1
        return False
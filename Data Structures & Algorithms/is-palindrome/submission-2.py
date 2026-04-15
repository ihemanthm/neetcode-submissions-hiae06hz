class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string = ""
        for char in s.lower():
            if ord(char)>=ord('a') and ord(char)<=ord('z'):
                valid_string+=char
            if ord(char)>=ord('0') and ord(char)<=ord('9'):
                valid_string+=char
        left, right = 0, len(valid_string)-1
        while left<right:
            if valid_string[left]!=valid_string[right]:
                return False
            left, right = left+1, right-1
        return True
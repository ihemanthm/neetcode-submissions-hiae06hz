class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        counters = {'(': ')', '[':']', '{':'}'}
        for each in s:
            if each in counters:
                stack.append(each)
            else:
                if not stack or each!=counters[stack[-1]]:
                    return False
                stack.pop()
        return not stack
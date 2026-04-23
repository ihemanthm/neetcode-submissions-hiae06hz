class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = list()
        result = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while mono and mono[-1][1]<temp:
                i, ele = mono.pop()
                result[i] = idx-i
            mono.append((idx, temp))
        return result
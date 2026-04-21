import math
class Solution:
    def is_power_of_two(self, num):
        log_val = math.log2(num)
        return int(log_val) == log_val
    def countBits(self, n: int) -> List[int]:
        counts = [0]*(n+1)
        latest_power_two = 0
        for num in range(1, n+1):
            if self.is_power_of_two(num):
                counts[num] = 1
                latest_power_two = num
            else:
                counts[num] = 1+counts[num-latest_power_two]
        return counts
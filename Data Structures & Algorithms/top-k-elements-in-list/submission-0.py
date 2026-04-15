class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_mapper = dict()
        for num in nums:
            count_mapper[num] = count_mapper.get(num,0)+1
        sorted_counts = sorted(count_mapper.items(), key = lambda x: x[1], reverse = True)
        
        res = [num for num,count in sorted_counts[:k]]

        return res
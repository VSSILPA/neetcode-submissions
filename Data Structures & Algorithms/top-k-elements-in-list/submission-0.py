class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for val in nums:
            counter[val] = counter.get(val, 0) + 1
        sorted_op = sorted(counter.items(), key = lambda x : x[1])
        return([x[0] for x in sorted_op[-k :]])        
        
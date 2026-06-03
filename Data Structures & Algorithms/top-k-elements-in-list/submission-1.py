class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for val in nums:
            counter[val] = counter.get(val, 0) + 1
        return([num for num, items in sorted(counter.items(), key =lambda x :x[1])[-k:]])
   
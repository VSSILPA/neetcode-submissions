class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) +1
        print(counts)
        for key, val in counts.items():
            if val > 1:
                return key
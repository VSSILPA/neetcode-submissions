class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # counts = dict()
        # for n in nums:
        #     counts[n] = counts.get(n, 0) +1
        # for key, val in counts.items():
        #     if val > 1:
        #         return key

        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                return abs(n)
            else:
                nums[index] = -1 * nums[index]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # s = set(range(1, len(nums)+1))
        # print(s)
        # return [each for each in s if each not in nums]

        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res
        
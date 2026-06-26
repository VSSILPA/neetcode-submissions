class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(range(1, len(nums)+1))
        print(s)
        return [each for each in s if each not in nums]
        
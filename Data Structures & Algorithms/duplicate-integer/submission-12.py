class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            try:
                count = counter[num]
                return True
            except KeyError:
                counter[num] = 1
        return False
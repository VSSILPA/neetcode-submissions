class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = collections.Counter(nums)
        max_length = 0
        for num in nums:
            cur_length = 0
            if num + max_length in num_dict:
                while num + cur_length in num_dict:
                    cur_length = cur_length + 1
                    if cur_length > max_length:
                        max_length = cur_length
        return max_length
    
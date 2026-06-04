class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest=0
        for val in numset:
            if (val-1) not in numset:
                length =1
                while (val + length) in numset:
                    length += 1

                if longest < length:
                    longest = length

        return longest
        
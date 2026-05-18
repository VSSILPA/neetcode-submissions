class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, val in enumerate(nums):
            if val not in lookup:
                lookup[val] = [index]
            else:
                cur_index = lookup[val]
                cur_index.append(index)
                lookup[val] = cur_index

        for first_index, num in enumerate(nums):
            second_num = target - num
            if second_num in lookup:
                second_indices = lookup[second_num]
                for second_index in second_indices:
                    if first_index!=second_index:
                        if first_index < second_index:
                            return [first_index, second_index]
                        else:
                            return [second_index, first_index]

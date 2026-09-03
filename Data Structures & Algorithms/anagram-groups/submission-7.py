class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                char_index = ord(char) - ord("a")
                count[char_index] += 1
            count = tuple(count)
            if count in ana_dict:
                ana_dict[count].append(s)
            else:
                ana_dict[count] = [s]
        all_val = []
        for values in ana_dict.values():
            all_val.append(values)
        return all_val
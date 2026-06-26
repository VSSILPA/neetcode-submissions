class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_list = []
        group_dict = {}
        for string in strs:
            count_array = [0 for x in range(26)]
            for char in string:
                count_array[ord(char)-97] = count_array[ord(char)-97] + 1
            count_array_tuple = tuple(count_array)
            if count_array_tuple in group_dict:
                anagram_list = group_dict[count_array_tuple]
                anagram_list.append(string)
                group_dict[count_array_tuple] = anagram_list
            else:
                group_dict[count_array_tuple] = [string]
        out = list(group_dict.values())
        return out

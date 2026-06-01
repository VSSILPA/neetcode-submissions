from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for each_str in strs:
            counts = [0] * 26
            for char in each_str:
                char_index = ord(char) - ord('a')
                counts[char_index] += 1
            
            counter[tuple(counts)].append(each_str)
        
        return(list(counter.values()))

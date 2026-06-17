from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            counts  = [0] * 26
            for char in s:
                counts[ord(char) - ord("a")] += 1
            # if tuple(counts) in d:
            d[tuple(counts)].append(s)

        return [*d.values()]
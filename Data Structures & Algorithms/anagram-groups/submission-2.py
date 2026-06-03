from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for each in strs:
            chars = [0]*26
            for c in each:
                chars[ord(c)- ord('a')] += 1
            cnt[tuple(chars)].append(each)
        return(list(cnt.values()))
       

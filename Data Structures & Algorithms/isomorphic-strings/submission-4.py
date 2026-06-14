class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        if len(s_counter.keys()) != len(t_counter.keys()):
            return False
        map_dict = {}
        for s_char, t_char in zip(s,t):
            if s_char not in map_dict:
                map_dict[s_char] = t_char
            else:
                val = map_dict[s_char]
                if val != t_char:
                    return False
        return True
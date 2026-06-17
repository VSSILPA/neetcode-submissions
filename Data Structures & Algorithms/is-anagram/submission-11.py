class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        s_d = {}
        t_d = {}
        for char in s:
            s_d[char]= s_d.get(char, 0) + 1
        for char in t:
            t_d[char] = t_d.get(char,0) + 1
        return s_d == t_d

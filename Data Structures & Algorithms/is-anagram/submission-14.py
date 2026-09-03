class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}

        if len(s) != len(t):
            return False

        for char in s:
            s_d[char] = s_d.get(char, 0) + 1

        for char in t:
            t_d[char] = t_d.get(char, 0) + 1

        if s_d == t_d:
            return True 
        else:
            return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) >= len(t):
            string1,string2 = s,t 
        else:
            string1,string2 = t,s 
        string1_counter = Counter(list(string1))
        string2_counter = Counter(list(string2))
        for key, value in string1_counter.items():
            if key in string2_counter:
                if value != string2_counter[key]:
                    return False
            else:
                return False
        return True

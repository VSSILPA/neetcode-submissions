class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        length=0
        substr = set()
        for R in range(len(s)):
            while s[R] in substr:
                substr.remove(s[L])
                L += 1

            substr.add(s[R])
            R+=1
            length= max(length, len(substr))
        
        return length
                
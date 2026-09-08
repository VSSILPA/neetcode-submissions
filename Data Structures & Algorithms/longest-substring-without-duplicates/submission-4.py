class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        R =0

        max_length = 0
        seen = set()
        while  R < len(s):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            seen.add(s[R])
            R+=1
            max_length = max(max_length, len(seen))
            # print(sub)
        return(max_length)
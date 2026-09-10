class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        R=0

        seen = set()
        max_length = 0
        while R < len(s):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            seen.add(s[R])
            max_length = max(max_length, len(seen))
            R += 1

        return max_length
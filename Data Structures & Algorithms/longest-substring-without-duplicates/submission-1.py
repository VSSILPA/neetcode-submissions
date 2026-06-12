class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            sub = set()
            sub.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in sub:
                    break
                sub.add(s[j])
            print(i)
            print(sub)
            length = max(length, len(sub))

        return length

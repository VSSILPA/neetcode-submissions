class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length =0
        L=0
        counter=dict()
        for R in range(len(s)):
            counter[s[R]] = counter.get(s[R], 0) +1
            substring = s[L:R+1]
            replacement =  len(substring) - max(counter.values())
            if replacement <= k:
                length = max(length, len(substring))
            else:
                counter[s[L]] -= 1
                L +=1

        return length 
        
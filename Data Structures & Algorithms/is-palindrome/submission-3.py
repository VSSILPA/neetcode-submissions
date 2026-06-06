class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([s_.lower() for s_ in s if s_.isalpha() or s_.isdigit()])
        L =0
        R= len(new_s) -1
        while L < R:
            if new_s[L] != new_s[R]:
                return False
            L +=1
            R-=1
        return True